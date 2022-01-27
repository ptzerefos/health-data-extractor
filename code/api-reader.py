import json
import csv
import requests
import pandas as pd

response = requests.get("https://health.data.ny.gov/resource/u4ud-w55t.json?hospital_service_area=Finger Lakes")
resp_json = response.json()

with open('data.json', 'w') as f:
    json.dump(resp_json, f)

#print(resp_json[0])

with open('data.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('fingerlakes.csv', encoding='utf-8', index=False)
