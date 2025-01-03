from pymongo import MongoClient
from config import MONGO_URI,MONGO_DATABASE
 
db_client = MongoClient(MONGO_URI)
db = db_client.get_database(MONGO_DATABASE)

def get_db():
    """Helper function to get the database connection."""
    return db
