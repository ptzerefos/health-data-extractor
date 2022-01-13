import json
import csv
import requests

response = requests.get("https://health.data.ny.gov/resource/u4ud-w55t.json")
print(response)
