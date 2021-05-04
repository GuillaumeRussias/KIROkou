###############
#add ./KIROKOU in path

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

###############

import json


def test_json_input():
    with open("Input/test.json","r") as json_file: #automatically close file
        json_dict = json.load(json_file)
    
    #json_dict is now a pure python dictionnary :
    print(json_dict.keys())
    for key,value in json_dict.items():
        print(key,value)
    return json_dict

test_json_input()