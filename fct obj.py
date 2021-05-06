

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

###############

import numpy as np
import load_input

a = load_input.Input('A')

"""
    attributs :
    - (list(dict)) trains : contient les groupes de trains de T. 
            ◦ id contient l’id de t (un entier ≥ 0)
            ◦ sensDepart contient un booléen égal à true si t ∈ T et false si t ∈ T a
            ◦ voieEnLigne contient `t
            ◦ voieAQuai contient une proposition pour qt (comme qt est une variable, celle-ci peut bien entendu être remise en cause)
            ◦ typeCirculation contient et
            ◦ typesMateriels contient la liste Mt
            ◦ dateHeure contient dt sous forme de strin
    - list(dict) itineraires  : contient les itinéraires de I. Pour chacun d’eux
            ◦ id contient l’id de i (un entier ≥ 0)
            ◦ sensDepart un booléen égal à true si i ∈ Id et false si i ∈ Ia
            ◦ voieEnLigne contient `i
            ◦  voieAQuai contient qi
    -list(str) voiesAQuai : contient la liste des voies à quai.
    -list(str) voiesEnLigne : contient la liste des voies en ligne.
    -list(dict) interdictionsQuais : contient les contraintes de quais de F. 
    Pour chacune,
            ◦ voiesAQuaiInterdites contient la liste Qf
            ◦ voiesEnLigne contient la liste Lf
            ◦ typesMateriels contient la liste Mf
            ◦ typesCirculation contient la liste Ef
    -list(tuple(int,int,int,int,int)) contraintes : contient les itinéraires 
    incompatibles de J . C’est une liste dont chaque élément correspond à un j 
    et vient sous la forme d’un quintuplet d’entiers [a,b,c,d,e] où
            ◦ a contient l’id de t1,j
            ◦ b contient l’id de i1,j
            ◦ c contient l’id de t2,j
            ◦ d contient l’id de i2,j
            ◦ e contient cj 
    """

c_virtual = 2000

def fct_obj(input_, trains_id_list, train_affect_list, train_itineraire_list):
    
    cost_virtural_ = virtual_cost(input_, trains_id_list, train_affect_list, train_itineraire_list)
    
    cost_intersect_ = cost_intersect_(input_, trains_id_list, train_affect_list, train_itineraire_list)
    return cost_virtural_ + cost_intersect_


def virtual_cost(input_, trains_id_list, train_affect_list, train_itineraire_list):
    return 2000*sum([ e =="notAffected" for e in train_affect_list])

def cost_tensor(input_):
    nb_trains = len([item for sublist in input_a.trains for item in sublist])
    nb_affects
    cost_tensor = np.zeros((len(trains_id_list),trains_id_list,trains_id_list,trains_id_list))

def cost_intersect_(input_, trains_id_list, train_affect_list, train_itineraire_list):
    c = 0.
    for i in range(len(trains_id_list)):
        for j in range(len(trains_id_list)):
            if i!=j:
                c+= 0
    return c
 







