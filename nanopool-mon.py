#!/usr/bin/env python3

import requests
import collections
import sys

url = "https://api.nanopool.org/v1/eth/user/{}".format(sys.argv[1])
req = requests.get(url)

data = req.json()["data"]

print("Account: " + data["account"])
print("Balance: " + data["balance"])
print("Current hashrate: " + data["hashrate"])