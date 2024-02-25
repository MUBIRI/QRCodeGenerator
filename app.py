#!/usr/bin/env python

"""
QR code generation API. Provides endpoints for generating QR codes and saving data to the database.

The '/' endpoint returns a simple GET response.

The '/qr_code' endpoint takes a JSON payload and generates a QR code image using the helper module. Returns filename of generated image.

The '/save_to_db' endpoint takes a JSON payload and saves it to the database after generating a QR code. Returns QR code filename.
"""

"""Contains the flask app"""

from flask import Flask, request, response
from models.helper import User

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """home route"""
    return "hello world"

@app.route("create_qr_code", methods=["POST"], strict_slashes=False)
def submit():
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
