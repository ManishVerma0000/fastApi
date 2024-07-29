from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URI = "mongodb://localhost:27017/"

def connect_to_mongodb():
    try:
        client = MongoClient(MONGO_URI)
        client.server_info()
        print("MongoDB connection successful")
        return client
    except ConnectionFailure as e:
        print(f"MongoDB connection error: {e}")
        raise e


import psycopg2
def conn():
    try:
        connection = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port=5432)
        print('connected')
    except Exception as e:
        print('connection failed',e)
