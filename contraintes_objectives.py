def find_in_1darray_where_id(array,_id):
        for i in range(len(array)):
            if array[i]["id"] == _id :
                return array[i]
        raise KeyError("itineraire_id not find")

def find_in_2darray_where_id(array,_id):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]["id"] == _id :
                return array[i][j]
    raise KeyError("train_id not find")




class isAdmissible():
    def __init__(_output,_input):
        self.output=_output
        self.input=_input
    
    def check_itineraire():
        for train_id,dico in self.output.items():
            itineraire_id = dico["itineraire"]
            voieAQuai_id = dico["voieAquai"]

            train = find_in_2darray_where_id(self.input.trains, train_id)
            voieEnLigne = train["voieEnLigne"]
            sensDepart = train["sensDepart "]
            
            itineraire_specs = find_in_1darray_where_id(self.input.itineraires, itineraire_id)
            if itineraire_specs["voieEnLigne"]!=voieEnLigne_id:
                raise Exception("voieEnLigne(input.intineraire)!=voieEnLigne(output) pour le meme itineraire")
            if itineraire_specs["voieAQuai"]!=voieAQuai_id:
                raise Exception("voieAQuai(input.itineraire)!=voieAQuai(output) pour le meme itineraire")
            if itineraire_specs["sensDepart"]!=sensDepart:
                raise Exception("les sens ne coincident pas")

    def check_interdictionQuai():
        for train_id,dico in self.output.items():
            voieAQuai_id = dico["voieAquai"]
            train = find_in_2darray_where_id(self.input.trains, train_id)
            voieEnLigne = train["voieEnLigne"]
            typeM_train = train["typesMateriels"]
            typeC_train = train["typeCirculation"]
            
            for interdiction in self.input.interdictionsQuais :
                if voieAQuai_id in interdiction[" voiesAQuaiInterdites"]:
                    if typeM_train in interdiction["typesMateriels"] :
                        raise Exception("Ce type de Materiel n'a pas le droit de stationner sur ce quai")
                    if typeC_train in interdiction["typesCirculation"] :
                        raise Exception("Ce type de Circulation n'a pas le droit de stationner sur ce quai")
                    if voieEnLigne in interdiction["voiesEnLigne"]:
                        raise Exception("la voie en ligne n'est pas reliee avec ce quai")
    def check_same_group():
        for group in self.input.trains :
            quai={}
            for train in group:
                train_id = group["id"]
                quai[self.output[str(train_id)]["voieAQuai"]] = 0
            if len(quai.keys())!=1:
                raise Exception("les trains d'un meme groupe doivent avoir le mem quai")  

    



    


