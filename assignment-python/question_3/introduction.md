# Configuration Management System

#### Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

## Requirements

- The program should read a configuration file (you can provide a sample configuration file).
- It should extract specific key-value pairs from the configuration file.
- The program should store the extracted information in a data structure (e.g., dictionary or list).
- It should handle errors gracefully in case the configuration file is not found or cannot be read.
- Finally, save the output file data as JSON data in the database.
- Create a GET request to fetch this information.

## Sample Configuration File

```ini
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
```

## Sample Output

```
Configuration File Parser Results:

Database:
- host: localhost
- port: 3306
- username: admin
- password: secret

Server:
- address: 192.168.0.1
- port: 8080
```


## Overview
This project provides a configuration management system using **Flask**, **MongoDB**, and **ConfigParser**. It reads configuration details from a `.ini` file, stores them in MongoDB, and serves the configurations via a REST API.

## Technologies Used
- Python
- Flask
- MongoDB
- ConfigParser
- PyMongo

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- MongoDB Atlas (or a local MongoDB instance)
- Required Python packages (see **Installation** section)

## Installation
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Create a `config.ini` file in the project directory with the required sections:
   ```ini
   [Database]
   host = localhost
   port = 27017
   username = admin
   password = password123

   [Server]
   address = 127.0.0.1
   port = 5000
   ```
4. Update MongoDB credentials in the script:
   ```python
   DB_USERNAME = "your_mongo_username"
   DB_PASSWORD = "your_mongo_password"
   ```

## Running the Application
1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Access the API endpoint:
   ```sh
   http://127.0.0.1:5000/config
   ```

## API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| GET    | `/config` | Fetches the configuration data from MongoDB |

## Error Handling
- If the configuration file is missing, an error message is displayed.
- If MongoDB connection fails, the script exits with an error.