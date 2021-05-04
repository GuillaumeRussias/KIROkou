###############
#add ./KIROKOU in path

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

###############



import json
#export en json??

def test_export():
    dict_to_export = {"clef1":1,"clef2":3,"clef3":["bonjour","les",1,False],"clef4": {"subclef4.1":"sousdictionnaire"}}
    str_json = json.dumps(dict_to_export)
    with open("Output/test.json","w") as json_file:
        json_file.write(str_json)

test_export()
    
