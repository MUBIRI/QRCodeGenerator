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