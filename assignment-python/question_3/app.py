import os
import json
import configparser
from pymongo import MongoClient
from flask import Flask, jsonify

# MongoDB Configuration
DB_USERNAME = "" # Enter your username
DB_PASSWORD = "" # Enter your password

MONGO_URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.w0uv8.mongodb.net/"
DB_NAME = "configDB"
COLLECTION_NAME = "configurations"

try:
    # Initialize MongoDB Client
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Read and parse configuration file
def parse_config(file_path):
    config = configparser.ConfigParser()
    
    if not os.path.exists(file_path):
        raise FileNotFoundError("Configuration file not found.")
    
    config.read(file_path)
    config_data = {}

    # Ensure required sections exist
    required_sections = ["Database", "Server"]
    for section in required_sections:
        if config.has_section(section):
            config_data[section] = dict(config.items(section))
        else:
            print(f"Warning: Section '{section}' is missing in the config file.")

    # Convert port values to integers
    if "Database" in config_data and "port" in config_data["Database"]:
        config_data["Database"]["port"] = int(config_data["Database"]["port"])

    if "Server" in config_data and "port" in config_data["Server"]:
        config_data["Server"]["port"] = int(config_data["Server"]["port"])

    return config_data

# Store data in MongoDB
def save_to_mongodb(data):
    collection.delete_many({})  # Clear existing data
    collection.insert_one(data)

# Create Flask App
app = Flask(__name__)

@app.route("/config", methods=["GET"])
def get_config():
    data = collection.find_one({}, {"_id": 0})  # Exclude MongoDB's default _id
    if data:
        formatted_output = {
            "Database": {
                "host": data["Database"]["host"],
                "port": data["Database"]["port"],
                "username": data["Database"]["username"],
                "password": data["Database"]["password"]
            },
            "Server": {
                "address": data["Server"]["address"],
                "port": data["Server"]["port"]
            }
        }
        return jsonify(formatted_output)
    
    return jsonify({"error": "No configuration data found."}), 404

if __name__ == "__main__":
    try:
        config_file_path = "config.ini"
        parsed_data = parse_config(config_file_path)
        save_to_mongodb(parsed_data)
        print("Configuration saved to MongoDB successfully!")
        
        # Run the Flask API
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")