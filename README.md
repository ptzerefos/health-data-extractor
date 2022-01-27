# health-data-extractor

## Purpose
For Lukie!

Query the following APIs for data:
https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/u4ud-w55t
  API URL - https://health.data.ny.gov/resource/u4ud-w55t
        JSON - https://health.data.ny.gov/resource/u4ud-w55t.json
        CSV  - https://health.data.ny.gov/resource/u4ud-w55t.csv

Transform the data
Export the data into a format suitable for SQL server per requirements

##Running the code
Step 1 - pull down data with filter Finger Lakes
Step 2 - put data into data frame
Step 3 - convert to csv
.
.
.
Step N - Push to SQL database (for Tableau)

## Prerequisites
Install Python (version 3.7+) on your local machine

run pip install -r requirements.txt

pip3 install requests
pip3 install pandas

## Getting Started
- Navigate to where you want your local version of the code to live.
- Clone the repository
    'git clone https://github.com/ptzerefos/health-data-extractor.git'


Adding an API

TODOs:
Build scalable/automate infrastructure for autonomous actions
