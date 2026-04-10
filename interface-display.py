# Menu du tournoi
def menu():
    print("=== TOURNOI ===")
    print("1. 4 joueurs")
    print("2. 8 joueurs")
    print("3. 16 joueurs")

    choix = input("Choix : ")

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

    # boucle pour demander les noms
    for i in range(nb):
        nom = input(f"Nom du joueur {i+1} : ")
        joueurs.append(nom)  # ajout dans la liste

    return joueurs


# programme principal
nb_joueurs = menu()
joueurs = saisir_joueurs(nb_joueurs)

# affichage pour vérifier
print("Liste des joueurs :", joueurs)