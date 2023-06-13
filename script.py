#!/usr/bin/env python3

import requests
import os

directory = '/data/feedback/'
files = os.listdir(directory)
keys = ["title", "name", "date", "feedback"]
parsed_feedback = []
web_url = "null"

def readfile(file):
    with open(directory, file) as f:
        line = f.read().splitlines()
    return line

for file in files:
    line = readfile(file)
    parsed_feedback.append(dict(zip(keys, line)))

for feedback in parsed_feedback:
    response = requests.post(web_url, data=feedback)
    if response.ok:
        print("Feedback logged successfully")
    else:
        print("Entry failed. Error code: {}".format({response.status.code}))

