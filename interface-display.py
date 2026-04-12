import time  # module pour ajouter des pauses dans le programme


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
            print("❌ mhmmmm NON. Entrez 1, 2 ou 3.")


def saisir_joueurs(nb):
    joueurs = []  # liste qui stocke les noms des joueurs

    for i in range(nb):
        # boucle jusqu'à ce que le nom soit valide
        while True:
            nom = input(f"Nom du joueur {i+1} : ").strip()
            if nom:
                joueurs.append(nom)
                break
            else:
                # empêche les noms vides
                print("❌ Le nom ne peut pas être vide.")

    return joueurs


def afficher_bracket(joueurs):
    print("\n" + "=" * 40)
    print("              MATCHS MATCHS MATCHS")
    print("=" * 40)

    # affiche les matchs 2 par 2 avec le pas de 2
    for i in range(0, len(joueurs), 2):
        print(f"{joueurs[i]} ──┐")
        print(f"         ├── Match {i//2 + 1}")
        print(f"{joueurs[i+1]} ──┘\n")


# point d'entrée du programme
nb_joueurs = menu()
joueurs = saisir_joueurs(nb_joueurs)

print("\nChargement du tournoi...")
time.sleep(1)  # pause d'une seconde pour l'effet de chargement

afficher_bracket(joueurs)