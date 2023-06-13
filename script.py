#!/usr/bin/env python3

import requests
import os

directory = '/data/feedback/'
files = os.listdir(directory)
parsed_feedback = []
keys = [title, name, date, feedback]

def readfile(file):
    with open(directory, file) as f:
        line = f.read().splitlines()
    return line



response = requests.get('https://www.google.com')
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))