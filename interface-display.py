''' Fonction : menu
role : afficher les options du tournoi
et récupérer le choix de l'utilisateur '''
def menu():
    print("=== TOURNOI ===")
    print("1. 4 joueurs")
    print("2. 8 joueurs")
    print("3. 16 joueurs")

    # Demande à l'utilisateur de choisir une option
    choix = input("Choix : ")

    # Affiche le choix pour vérification
    print("Tu as choisi l'option :", choix)


# Appel de la fonction pour lancer le menu
menu()