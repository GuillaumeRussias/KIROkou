###############
#add ./KIROKOU in path

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

###############

import json
import numpy


class Input():
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
            ◦ voieAQuai contient qi
    -list(str) voiesAQuai : contient la liste des voies à quai.
    -list(str) voiesEnLigne : contient la liste des voies en ligne.
    -list(dict) interdictionsQuais : contient les contraintes de quais de F. Pour chacune,
            ◦ voiesAQuaiInterdites contient la liste Qf
            ◦ voiesEnLigne contient la liste Lf
            ◦ typesMateriels contient la liste Mf
            ◦ typesCirculation contient la liste Ef
    -list(tuple(int,int,int,int,int)) contraintes : contient les itinéraires incompatibles de J . C’est une liste dont chaque élément correspond à un j et vient sous la forme d’un quintuplet d’entiers [a,b,c,d,e] où
            ◦ a contient l’id de t1,j
            ◦ b contient l’id de i1,j
            ◦ c contient l’id de t2,j
            ◦ d contient l’id de i2,j
            ◦ e contient cj 
    """
    def __init__(self,name_input = "A", path_input = "Input/instances"):
        with open(f"{path_input}/{name_input}.json","r") as json_file:
            self.__dict__ = json.load(json_file)
    
    def get_list_train(self):
        return numpy.concatenate(self.trains)
    def get_list_train_id(self):
        return [t["id"] for t in g for g in self.trains]


    
    
input_a = Input("A")




