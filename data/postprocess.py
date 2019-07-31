import pandas as pd
import json_lines as jl
from sys import argv
import logging

if len(argv) < 3:
    logging.critical('Not enough parameters passed. Run script as:\npython postprocess.py [input-file] [output-directory]')
    exit(1)

parcel_items = []
building_items = []


with open('../scraper/parceldata.jl', 'rb') as f:
    for item in jl.reader(f):
        if not item:
            #pass over empty dictionary
            continue
        elif 'property_address' in item:
            pass
        elif 'use_code' in item:
            pass
        elif 'millage_rate' in item:
            pass
        elif 'owner' in item:
            pass