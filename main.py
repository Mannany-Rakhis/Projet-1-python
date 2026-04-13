import random
import time

# ─── LOGIQUE (Noémie) 
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

# ─── INTERFACE (Mannany)

def menu():
    # affiche les options du tournoi
    print("=== TOURNOI ===")
    print("1. 4 joueurs")
    print("2. 8 joueurs")
    print("3. 16 joueurs")

    # boucle jusqu'à ce que l'utilisateur entre un choix valide
    while True:
        choix = input("Choix (1/2/3) : ").strip()
        if choix == "1":
            return 4
        elif choix == "2":
            return 8
        elif choix == "3":
            return 16
        else:
            # message d'erreur si le choix est invalide
            print("☠️ mhmmmm NON. Entrez 1, 2 ou 3.")

def saisir_joueurs(nb):
    joueurs = []  # liste qui stocke les noms des joueurs

    for i in range(nb - 1):
        # boucle jusqu'à ce que le nom soit valide
        while True:
            nom = input(f"Nom du joueur {i+1} : ").strip()
            if nom:
                # adapté au format dictionnaire de la collègue
                joueurs.append({"nom": nom, "type": "H"})
                break
            else:
                # empêche les noms vides
                print("❌ Le nom ne peut pas être vide.")

    # le dernier joueur est toujours une IA
    joueurs.append({"nom": "Terminator-IA 🤖 ", "type": "IA"})
    return joueurs

def afficher_bracket(joueurs):
    print("\n" + "=" * 40)
    print("              MATCHS MATCHS MATCHS")
    print("=" * 40)

    # affiche les matchs 2 par 2 avec le pas de 2
    for i in range(0, len(joueurs), 2):
        print(f"{joueurs[i]['nom']} ──┐")
        print(f"         ├── Match {i//2 + 1}")
        print(f"{joueurs[i+1]['nom']} ──┘\n")

# ─── PROGRAMME PRINCIPAL 

nb_joueurs = menu()
joueurs = saisir_joueurs(nb_joueurs)

print("\nChargement du tournoi...")
time.sleep(1)  # pause d'une seconde pour l'effet de chargement

afficher_bracket(joueurs)

# boucle du tournoi récupérée de la collègue
while len(joueurs) > 1:
    print(f"\n IL RESTE {len(joueurs)} JOUEURS EN LICE")
    vainqueurs_du_tour = []

    for i in range(0, len(joueurs), 2):
        gagnant = faire_un_match(joueurs[i], joueurs[i+1])
        vainqueurs_du_tour.append(gagnant)
        print(f" {gagnant['nom']} gagne le match et passe au tour suivant !")

    joueurs = vainqueurs_du_tour

print(f"\nVICTOIRE FINALE DE : {joueurs[0]['nom']} 🏅 Félicitations mon gars ! 🎉") 