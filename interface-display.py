# Menu du tournoi
def menu():
    print("=== TOURNOI ===")
    print("1. 4 joueurs")
    print("2. 8 joueurs")
    print("3. 16 joueurs")

    choix = input("Choix : ")  # récupération du choix

    # on retourne le nombre de joueurs correspondant
    if choix == "1":
        return 4
    elif choix == "2":
        return 8
    elif choix == "3":
        return 16
    else:
        return 4  # valeur par défaut si erreur


# appel du menu
nb_joueurs = menu()

print("Nombre de joueurs :", nb_joueurs)