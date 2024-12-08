from pymongo import MongoClient


def initialize_db():
    client = MongoClient('mongodb+srv://manahilmano2002:helloworld@cluster0.nconi13.mongodb.net/')
    db = client['Mlops_project']  # Change 'userData' to your desired database name

    # Create a collection and add some initial data
    users_collection = db['users']


    client.close()

if __name__ == "__main__":
    initialize_db()