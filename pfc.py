import random
def demander_choix(nom_du_joueur):
    choix = ""
    while choix != "P" and choix != "F" and choix != "C":
        choix = input(f"{nom_du_joueur}, entrez P, F ou C : ").upper().strip()
        if choix != "P" and choix != "F" and choix != "C":
            print("Erreur ! Tu dois écrire P, F ou C.")
    return choix
def qui_gagne(c1, c2):
    if c1 == c2:
        return "égalité"
    if (c1 == "P" and c2 == "C") or \
       (c1 == "F" and c2 == "P") or \
       (c1 == "C" and c2 == "F"):
        return "joueur1"
    else:
        return "joueur2"

def faire_un_match(joueur_a, joueur_b):
    points_a = 0
    points_b = 0
    
    print(f"\n MATCH : {joueur_a['nom']} VS {joueur_b['nom']} ")
    
    while points_a < 2 and points_b < 2:
        if joueur_a['type'] == "H":
            choix_a = demander_choix(joueur_a['nom'])
        else:
            choix_a = random.choice(["P", "F", "C"])
            
        if joueur_b['type'] == "H":
            choix_b = demander_choix(joueur_b['nom'])
        else:
            choix_b = random.choice(["P", "F", "C"])
            
        print(f"{joueur_a['nom']} ({choix_a}) VS {joueur_b['nom']} ({choix_b})")
        
        resultat = qui_gagne(choix_a, choix_b)
        
        if resultat == "joueur1":
            points_a = points_a + 1
            print(f"Point pour {joueur_a['nom']} !")
        elif resultat == "joueur2":
            points_b = points_b + 1
            print(f"Point pour {joueur_b['nom']} !")
        else:
            print("Égalité ! On refait la manche.")
            
        print(f"Score actuel : {points_a} - {points_b}")

    if points_a == 2:
        return joueur_a
    else:
        return joueur_b

def lancer_le_tournoi():
    print(" Welcome to Rock, Paper, Scissors!")
    
    reponse = input("Entrer le nombre de participants:")
    if reponse != "4" and reponse != "8" and reponse != "16":
        print("Ce nombre n'est pas valide!!.")
        return
    
    nb_total = int(reponse)
    liste_joueurs = []
    
    for i in range(nb_total - 1):
        nom = input(f"Nom du joueur {i+1} : ")
        if nom == "":
            nom = f"Joueur {i+1}"
        liste_joueurs.append({"nom": nom, "type": "H"})
        
    liste_joueurs.append({"nom": "Terminator-IA", "type": "IA"})
    
    random.shuffle(liste_joueurs)
    
    while len(liste_joueurs) > 1:
        print(f"\n IL RESTE {len(liste_joueurs)} JOUEURS EN LICE")
        vainqueurs_du_tour = []
    
        for i in range(0, len(liste_joueurs), 2):
            gagnant = faire_un_match(liste_joueurs[i], liste_joueurs[i+1])
            vainqueurs_du_tour.append(gagnant)
            print(f" {gagnant['nom']} gagne le match et passe au tour suivant !")
            
        liste_joueurs = vainqueurs_du_tour

    print(f"\nVICTOIRE FINALE DE : {liste_joueurs[0]['nom']} ! Félicitations !")
lancer_le_tournoi()