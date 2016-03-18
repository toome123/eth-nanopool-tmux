#!/usr/bin/env python3

import requests
import collections
import sys

url = "http://nanopool.org/api/user/{}".format(sys.argv[1])
req = requests.get(url)

data = req.json()["data"]

print("Account: " + data["account"])
print("Balance: " + data["balance"])
print("Current hashrate: " + data["hashrate"])

for worker in data["workers"]:

    worker = collections.OrderedDict(sorted(worker.items()))
    print("\nWorker: " + worker["id"])
    print("Individual hashrate: " + worker["hashrate"])
    for k, v in worker.items():
        if (k != "id") and (k != "hashrate"):
            k = k.split("_")
            k[0] = k[0].replace("avg", "Average")
            k[1] = k[1].upper()
            print(k[0] + " " + k[1] + ": " + v)
