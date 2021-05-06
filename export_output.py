###############
#add ./KIROKOU in path

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

###############



import json
#export en json??

class Output():
    def __init__(self,trains_id_list,train_affect_list,train_itineraire_list,name_export="A"):
        self.json_dict={}
        self.name = name_export
        for i in range(len(trains_id_list)):
            id_ = trains_id_list[i]
            affect_ = train_affect_list[i]
            itineraire_ = train_itineraire_list[i]
            self.json_dict[str(id_)]= {" voieAQuai ": affect_," itineraire ":itineraire_}
        
    def export(self):
        json_str = json.dumps(self.json_dict)
        with open(f"Output/{self.name}.json","w") as json_file:
            json_file.write(json_str)
        
export_a=Output([1,2,3,4],[" notAffected "," notAffected "," notAffected "," notAffected "],[" notAffected "," notAffected "," notAffected "," notAffected "],"a")
export_a.export()