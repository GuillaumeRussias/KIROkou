# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:29:02 2021

@author: robin
"""


import numpy as np
import load_input
import contraintes_objectives
import random as r

input_ = load_input.Input("A")


nb_trains = len([item for sublist in input_.trains for item in sublist])
nb_itineraires = len(input_.itineraires)

sol = np.zeros(nb_trains, dtype = int)


cost = 0  # a changer !!!!!!!!!!!!!!!!!!!!!!!
for i in range(nb_trains):
    print("iteration : ",i)
    id_next = r.randint(0, nb_itineraires)
    print("id_next : ", id_next)
    if (np.isin(id_next, sol)):
        id_old = sol[i]
        sol[i] = id_next
        cost = 0 #  à changer !!!!!!!!!!!!!!!!!!!!!!
        
        
        
    
    