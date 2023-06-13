#!/usr/bin/env python3

import requests

response = requests.get('https://www.google.com')
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))