import os

from flask import Flask, jsonify
from flask_cors import CORS 
from dotenv import load_dotenv # Import dotenv to load environment variables from an optional .env file.

load_dotenv() 

app = Flask(__name__)

CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for the Flask app.

@app.route("/products", methods=["GET"])  # Define a route for the "/products" endpoint that accepts GET requests.
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},  # Product 1: Dog Food
        {"id": 2, "name": "Cat Food", "price": 34.99},  # Product 2: Cat Food
        {"id": 3, "name": "Bird Seeds", "price": 10.99},  # Product 3: Bird Seeds
    ]
    
    return jsonify(products) # Return a JSON response containing a list of product objects.

if __name__ == "__main__":  # Check if the script is being run directly (not imported as a module).
    port = int(os.environ.get("PORT", 3030))  # Get the port from environment variables or default to 3030.
    
    app.run(host="0.0.0.0", port=port)


    