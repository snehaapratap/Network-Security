
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://snehapratap248:mongodb@cluster0.3v0xzwb.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)