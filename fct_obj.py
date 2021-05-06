

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

###############

import numpy as np
import load_input
import pandas


c_virtual = 2000

class objectiv_func:
    def __init__(self,_input):
        self.input=_input
        self.pd_contraintes = pandas.DataFrame(self.input.contraintes)
        self.pd_contraintes.rename(columns={0:"t1",1:"i1",2:"t2",3:"i2",4:"c"},inplace=True)
   
    def get_affected_cost(self,I):
        cost = 0
        for i in range (len(I)):
            itin = I[i]
            potential_cost_1 = self.pd_contraintes[self.pd_contraintes["i1"]==itin && self.pd_contraintes["t1"]==i].index
            for j in potential_cost_1 :
                t2 = self.pd_contraintes["t2"][j]
                i2 = self.pd_contraintes["i2"][j]
                if I[t2]==i2 :
                    cost += self.pd_contraintes["c"][j]            
        return cost
    
    def __call__(self,I):
        nonaffected_cost = 2000*np.isin(I,["notAffected"]).sum()
        affected_cost = self.get_affected_cost(I)
        return nonaffected_cost + affected_cost


print("a")
g = objectiv_func(a, a.get_list_train_id())




