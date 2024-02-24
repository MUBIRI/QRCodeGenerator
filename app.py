"""
QR code generation API. Provides endpoints for generating QR codes and saving data to the database.

The '/' endpoint returns a simple GET response.

The '/qr_code' endpoint takes a JSON payload and generates a QR code image using the helper module. Returns filename of generated image.

The '/save_to_db' endpoint takes a JSON payload and saves it to the database after generating a QR code. Returns QR code filename.
"""
#!/usr/bin/env python

"""Contains the flask app"""
from flask import Flask, request
from models import helper 
# The helper file contains our generate uuid and qr code generator

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "GET":
        print("Get")
        return ({"message": "GET"})

@app.route("/qr_code", methods=["POST"])
def qr_code():
    try:
        data = request.get_json()
        filename = helper.generate_qr_code(**data)
        return ({"message": "QR code generated", "filename": filename})
    
    except Exception as e:
        return e

@app.route("/save_to_db", methods=["POST"])
def save_to_db(data):
    try:
        data = request.get_json()
        filename = helper.generate_qr_code(**data)
        return ({"message": "QR code generated", "filename": filename})
    
    except Exception as e:
        return e