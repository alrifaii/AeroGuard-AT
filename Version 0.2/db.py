from pymongo import MongoClient
import json
import os

# MongoDB URI from environment variable (never store credentials in git)
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI is not set. Define it as an environment variable.")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)

# Access the "Clusters" database
db = client["Clusters"]

# Create or access the "locations" collection
locations_collection = db["locations"]

# Function to load a test JSON file and insert it into MongoDB
def load_and_insert_json(file_path):
    # Load the JSON data from a file
    with open(file_path, "r") as file:
        data = json.load(file)  # Convert JSON data into a Python dictionary
    
    # Insert the data into the MongoDB collection
    locations_collection.insert_many(data)  # Use insert_many for inserting multiple records

    print("Data inserted successfully.")

# Call the function and provide the path to your test JSON file
load_and_insert_json("locations.json")
