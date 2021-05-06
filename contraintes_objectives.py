
class isAdmissible():
    def __init__(_input):
        self.input=_input
        self.put_itineraires_in_dict()
        self.put_trains_in_dict()
    
    def put_trains_in_dict(self):
        self.trains={}
        for group in self.input.trains :
            for train in group:
                self.trains[str(train["id"])] = train

    def put_itineraires_in_dict(self):
        self.itineraires={}
        for iti in self.input.itineraires :
            self.itineraires[str(iti["id"])] = iti
    
    def check_itineraire(output):
        for train_id,dico in output.items():
            itineraire = dico["itineraire"]
            itineraire_specs = self.itineraire[str(itineraire)]
            train = self.train[train_id]

            voieAQuai = dico["voieAquai"]           
            voieEnLigne = train["voieEnLigne"]
            sensDepart = train["sensDepart "]

            if VoieAQuai == "notAffected" and itineraire=="notAffected" :
                continue

           
            if itineraire_specs["voieEnLigne"]!=voieEnLigne:
                raise Exception("voieEnLigne(input.intineraire)!=voieEnLigne(output) pour le meme itineraire")
            if itineraire_specs["voieAQuai"]!=voieAQuai:
                raise Exception("voieAQuai(input.itineraire)!=voieAQuai(output) pour le meme itineraire")
            if itineraire_specs["sensDepart"]!=sensDepart:
                raise Exception("les sens ne coincident pas")
        return True

    def check_interdictionQuai(output):
        for train_id,dico in output.items():
            voieAQuai = dico["voieAquai"]
            train = self.train[train_id]
            voieEnLigne = train["voieEnLigne"]
            typeM_train = train["typesMateriels"]
            typeC_train = train["typeCirculation"]
            
            for interdiction in self.input.interdictionsQuais :
                if voieAQuai in interdiction["voiesAQuaiInterdites"]:
                    if typeM_train in interdiction["typesMateriels"] :
                        raise Exception("Ce type de Materiel n'a pas le droit de stationner sur ce quai")
                    if typeC_train in interdiction["typesCirculation"] :
                        raise Exception("Ce type de Circulation n'a pas le droit de stationner sur ce quai")
                    if voieEnLigne in interdiction["voiesEnLigne"]:
                        raise Exception("la voie en ligne n'est pas reliee avec ce quai")
        return True

    def check_same_group(output):
        for group in self.input.trains :
            quai={}
            for train in group:
                train_id = group["id"]
                quai[output[str(train_id)]["voieAQuai"]] = 0
            if len(quai.keys())!=1:
                raise Exception("les trains d'un meme groupe doivent avoir le meme quai")  
        return True

    



    


