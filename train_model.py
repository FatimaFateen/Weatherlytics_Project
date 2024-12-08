import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
import pickle
from mlflow.tracking import MlflowClient


def train_model():
    # Load data
    df = pd.read_csv('processed_data.csv')
    X = df[['Humidity', 'Wind Speed']]
    y = df['Temperature']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Evaluate model
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)

    # Set up MLFlow
    mlflow.set_tracking_uri("http://localhost:5000")  # Adjust for remote server
    mlflow.set_experiment("Weather Prediction")

    with mlflow.start_run() as run:
        # Log parameters, metrics, and the model
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_param("features", ['Humidity', 'Wind Speed'])
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

        print("Model logged to MLFlow")

        # Get the run ID
        run_id = run.info.run_id

        # Register the model in the Model Registry
        client = MlflowClient()
        model_uri = f"runs:/{run_id}/model"
        registered_model = client.create_registered_model("WeatherPredictionModel")
        result = client.create_model_version(
            name="WeatherPredictionModel",
            source=model_uri,
            run_id=run_id
        )
        print(f"Model registered with version: {result.version}")

        # Optionally transition the model to a specific stage
        client.transition_model_version_stage(
            name="WeatherPredictionModel",
            version=result.version,
            stage="Staging"
        )
        print(f"Model transitioned to Staging stage.")

    # Save locally for pipeline continuity
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved locally to model.pkl")


if __name__ == "__main__":
    train_model()
