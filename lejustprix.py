# coding=utf-8


objets = {"ordinateur": 2000, "iphone": 1400, "godemichet": 200, "womanizer": 350}

print(objets["ordinateur"])

vitrine = 0 

for objet in objets.values():
    vitrine += objet
    print(vitrine)

limite = 10
tours = 0

while tours < limite:
    prix = int(input("Quel est le juste prix?"))
    if prix > vitrine:
        print("C'est moins!")
    elif prix < vitrine :
        print("C'est plus!")    
    else: 
        print("C'est gagné!")
        tours = 10
    tours += 1
    if tours < (limite-2):
        print(f"Heureusement, il te reste {tours} essais")
    elif tours < limite:
        print(f"Attention, tu n'as plus que {tours} essais")
    elif tours == limite: 
        print ("C'est perdu!")