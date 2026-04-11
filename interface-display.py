import time  # c'est pour ajouter une pause de chargement


# Menu du tournoi
def menu():
    print("=== TOURNOI ===")
    print("1. 4 joueurs")
    print("2. 8 joueurs")
    print("3. 16 joueurs")

    choix = input("Choix : ") 

    # retourne le nombre de joueurs
    if choix == "1":
        return 4
    elif choix == "2":
        return 8
    elif choix == "3":
        return 16
    else:
        return 4  # valeur par défaut


# Saisie des joueurs
def saisir_joueurs(nb):
    joueurs = []  

    # boucle pour entrer les noms
    for i in range(nb):
        nom = input(f"Nom du joueur {i+1} : ")
        joueurs.append(nom) 

    return joueurs


# Affichage du bracket
def afficher_bracket(joueurs):
    print("\n" + "=" * 40)
    print("              MATCHS MATCHS MATCHS")
    print("=" * 40)

    # affiche les matchs 2 par 2
    for i in range(0, len(joueurs), 2):
        print(f"{joueurs[i]} ──┐")
        print(f"         ├── Match {i//2 + 1}")
        print(f"{joueurs[i+1]} ──┘\n")


# Programme principal
nb_joueurs = menu()  # choix du nombre de joueurs
joueurs = saisir_joueurs(nb_joueurs)  # récuperer les noms

print("\nChargement du tournoi...")
time.sleep(1)  # petite pause 

afficher_bracket(joueurs)  # affichage du bracket