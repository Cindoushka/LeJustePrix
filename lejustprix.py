# coding=utf-8

objets = {"ordinateur": 2000, "iphone": 1400, "godemichet": 200, "womanizer": 350}

print(objets["ordinateur"])

vitrine = 0 

for objet in objets.values():
    vitrine += objet

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

