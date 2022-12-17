#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
# REST-API
# Title: API to save measured data to influxdb
# Author: Vojtěch Petrásek
# Generated: 17/12/2022 18:50:21
###################################################

from datetime import datetime
import sys

from flask import Flask, request

app = Flask(__name__)

@app.route("/api/v1/goodwe", methods=["POST"])
def post_data():
    print(request.json)
    return {"status": "ok"}

@app.route("/")
def home():
    return "Welcome to FVE api"

while(True):
    try:
        app.run(host='0.0.0.0', port=8000)
    except Exception as e:
        print(e)
        sys.exit()