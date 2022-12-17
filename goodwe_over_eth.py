#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
# Data extractor from goodwe
# Title: Read data via RS485 from goodwe
# Author: Vojtěch Petrásek
# Generated: 17/12/2022 18:50:21
###################################################

import asyncio
from datetime import datetime
import sys
import time

import goodwe
import requests

def main():
    while(True):
        try:
            print("a")
        except Exception as e:
            print(e)
        time.sleep(1)

while(True):
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit()