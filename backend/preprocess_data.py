import pandas as pd

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df['Temperature'] = (df['Temperature'] - df['Temperature'].mean()) / df['Temperature'].std()
    df['Wind Speed'] = (df['Wind Speed'] - df['Wind Speed'].mean()) / df['Wind Speed'].std()
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data('raw_data.csv', 'processed_data.csv')