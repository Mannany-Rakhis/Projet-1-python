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
        return 4


# Saisie des joueurs
def saisir_joueurs(nb):
    joueurs = []

    # boucle pour entrer les noms
    for i in range(nb):
        nom = input(f"Nom du joueur {i+1} : ")
        joueurs.append(nom)

    return joueurs


# Affichage d’un tour
def afficher_tour(joueurs, nom_tour):
    print(f"\n=== {nom_tour} ===")

    # affiche les matchs 2 par 2
    for i in range(0, len(joueurs), 2):
        print(joueurs[i], "vs", joueurs[i+1])


# Programme principal
nb_joueurs = menu()
joueurs = saisir_joueurs(nb_joueurs)

# affichage du premier tour
afficher_tour(joueurs, "Premier tour")