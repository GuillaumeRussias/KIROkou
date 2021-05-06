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


    


