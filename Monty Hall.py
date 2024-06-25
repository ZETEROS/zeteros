#Monty Hall Demonstration

import random

#Preparation d'univers
number_simulations = int(input("Combien de simulations il y aura ? \n"))
nombre_portes = 3 #Don't change yet.

#Compteurs
fois_gagnées_en_changeant = 0
fois_gagnées_en_gardant = 0

#Placement du prix derriere d'une des portes.
for _ in range(number_simulations):
    portes = [0] * nombre_portes
    price = random.randint(0, nombre_portes -1 )
    portes[price] = 1

    #Choix du joueur.
    choix = random.randint(0, nombre_portes -1)

    #Presentateur montre une des portes
    portes_montrables = [i for i in range(nombre_portes) if i != choix and portes[i] == 0]
    porte_montré = random.choice(portes_montrables)

    #changement de porte
    portes_restantes = [i for i in range(nombre_portes) if i != porte_montré and i != choix]
    nouveau_choix = random.choice(portes_restantes)

    #Verification finale, gagnant ou non.
    if portes[choix] == 1 :
        fois_gagnées_en_gardant += 1
    if portes[nouveau_choix] == 1 :
        fois_gagnées_en_changeant += 1

#Montrer les resultats.
Frequence_ch = fois_gagnées_en_changeant / number_simulations
Frequence_ga = fois_gagnées_en_gardant / number_simulations
print("\n\nNombre de fois gagnée en changeant = " , fois_gagnées_en_changeant)
print("Nombres de fois gagnées en gardant le choix initial = " , fois_gagnées_en_gardant)
print("\nRapport de victoires en changeant sur victoires en gardant \n" , fois_gagnées_en_changeant / fois_gagnées_en_gardant, "\n\n")
print("Frequences experimentales \nFrequence de victoire en changeant" , Frequence_ch," ==> ",Frequence_ch * 100,"%")
print("Frequence de victoire en gardant" , Frequence_ga, " ==> ",Frequence_ga * 100,"%")
