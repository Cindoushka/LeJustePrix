# coding=utf-8


class ObjetsDeLaVitrine() :
    nom: str
    prix: int

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

objets = [
        ObjetsDeLaVitrine("ordinateur", 2000), 
        ObjetsDeLaVitrine("iphone", 1400), 
        ObjetsDeLaVitrine("godemichet", 200), 
        ObjetsDeLaVitrine("womanizer", 350)
        ]


vitrine = 0 

for objet in objets:
    vitrine += objet.prix




def jeu():
    limite = 10
    tours = 0
    while tours < limite:
        try: prix = int(input("Quel est le juste prix?"))

        except ValueError:
            print("Vous devez proposer un nombre entier positif")
            tours == tours
            continue 
        if prix > vitrine:
            print("C'est moins!")
        elif prix < vitrine :
            print("C'est plus!")    
        else: 
            print("C'est gagné!")
            tours = 10
        tours += 1
        print(tours)
        if tours < (limite-2):
            print(f"Heureusement, il te reste {limite-tours} essais")
        elif tours < limite:
            print(f"Attention, tu n'as plus que {limite-tours} essais")
        elif tours == limite: 
            print ("C'est perdu!")


jeu() 
