#!/usr/bin/python3

#KG404 TraderBOT v1
#Get the basic JSON input/output features in place

import json
import sys

config = sys.argv[1]

def read_json():
    with open(config, 'r') as config_data:
        print("Able to read config file data.")
    
def write_json():
    open_file = {'version':'0.1'}
    with open(config, 'w') as output_data:
        json.dump(open_file, output_data)
        print("Generated output data.")


debug = read_json()
debug2 = write_json()
