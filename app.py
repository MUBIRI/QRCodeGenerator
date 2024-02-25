#!/usr/bin/env python

"""
QR code generation API. Provides endpoints for generating QR codes and saving data to the database.

The '/' endpoint returns a simple GET response.

The '/qr_code' endpoint takes a JSON payload and generates a QR code image using the helper module. Returns filename of generated image.

The '/save_to_db' endpoint takes a JSON payload and saves it to the database after generating a QR code. Returns QR code filename.
"""

"""Contains the flask app"""

from flask import Flask, request, response
from models.helper import User, generate_qr_code
from upload import upload

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """home route"""
    return "hello world"

@app.route("/create_qr_code", methods=["POST"], strict_slashes=False)
def submit():
    """Expects a json data, creates the qr_code, save it in the db"""
    data = request.get_json(silent=True)
    filename, employee_information = generate_qr_code(**data)
    upload(filename, employee_information)


@app.route("/fetch_qr_code/<database_id>", methods=["GET"], strict_slashes=False)
def get_code(database_id):
    """fetches the qr_code from the database"""
    # TODO create a function that fetch a particular qrcode using the id 
    result = get_code(database_id)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)

