from db_request import *

while True:
    print("\n-------------  Menu principal -------------\n")

    print("""
        1. Menu Consoles
        2. Menu des Jeux
        3. Quitter
        """)

    mp = input("Votre choix ? ")

    # Console Section
    if mp == "1":
        print("\n------------- Menu Consoles -------------\n")

        while True:
            print("""
                    1. Afficher toutes les consoles
                    2. Insérer une console
                    3. Mettre à jour une console
                    4. Supprimer une console
                    5. Chercher un console
                    6. Menu principal
                    """)

            mc = input("Votre choix ? ")

            # Print all consoles
            if mc == "1":
                print("\n------------- Liste des Consoles -------------\n")
                allConsole()

            # Add one console
            elif mc == "2":
                print("\n------------- Ajouter une console -------------\n")

                try:
                    name = input("Nom de la console: ")
                    manufacturer = input("Fabricant de la console: ")
                    console = Console(name=name, manufacturer=manufacturer)
                    insertConsole(console)
                    print("\nLa console à bien été ajoutée ")

                except:
                    print("\nDonnées de la console erroné. Veuillez réessayer")

            # Update a console
            elif mc == "3":
                print("\n------------- Mise à jour d'une console -------------\n")

                print("\nListe des consoles existantes\n")
                allConsole()

                try:
                    __id = input("\nL'id de la console à modifier: ")
                    name = input("Nouveau nom de la console: ")
                    manufacturer = input("Nouveau fabricant: ")
                    updateConsole(__id, name, manufacturer)
                    print("\nMise à jour effectuée avec succes")

                except:
                    print("""\n--- Soit les données de la console sont erronés, dans ce cas,
                          veuillez réessayer avec des données valides.\n"
                          --- Soit cette console n'existe pas.
                          Veuillez indiquer l'id d'une console parmi les consoles afficher""")

            # Delete one console
            elif mc == "4":
                print("\n------------- Supprimer une console -------------\n")

                print("\nListe des consoles existant\n")
                allConsole()

                try:
                    __id = input("\nL'id de la console à supprimer: ")
                    deleteConsole(__id)
                    print("\nLa console a bien été supprimée ")

                except:
                    print("\nCette console n'existe pas."
                          "Veuillez indiquer l'id d'une console parmi les consoles afficher")

            # Search a console
            elif mc == "5":
                print("\n------------- Chercher une console -------------\n")

                name = input("\nEntrer le nom de la console que vous recherchez: ")
                try:
                    console = searchConsole(name)
                    print("\nRésultat de la recherche: ")
                    print("""
                    Nom : {}
                    Fabricant: {}
                    Liste des jeux de cette console: """.format(console.name, console.manufacturer))
                    for game in console.games:
                        print("""
                        -- {}""".format(game.name))

                except:
                    print("\nCette console n'existe pas."
                          "Veuillez réessayer: ")

            # back
            elif mc == "6":
                break

            else:
                print("\nCette commande n'exite pas. Veuillez réessayer avec une commande valide")

    # Game Section
    if mp == "2":
        print("\n------------- Menu Jeux -------------\n")

        while True:
            print("""
                    1. Afficher tous les Jeux
                    2. Insérer un jeu
                    3. Mettre à jour un jeu
                    4. Supprimer un jeu
                    5. Chercher un jeu
                    6. Menu principal
                    """)

            mg = input("Votre choix ? ")

            # Print all games
            if mg == "1":
                print("\n------------- Liste des Jeux -------------\n")
                allgames()

            # Add one game
            elif mg == "2":
                print("\n------------- Ajouter un jeu -------------\n")

                try:
                    name = input("Nom du jeu: ")
                    description = input("Description du jeu: ")

                    print("\nListe des consoles existant\n")
                    allConsole()
                    __id = input("\nL'id de la console de ce jeu (parmi celles afficher): ")

                    insertGame(name, description, __id)
                    print("\nLe jeu a bien été ajouté ")

                except:
                    print("\nDonnées du jeu erroné. Veuillez réessayer")

            # Update a game
            elif mg == "3":
                print("\n------------- Mise à jour du jeu -------------\n")

                print("\nListe des jeux existant\n")
                allgames()

                try:
                    __id = input("\nL'id du jeu à modifier: ")
                    name = input("Nouveau nom du jeu: ")
                    description = input("Nouvelle description: ")

                    print("\nListe des consoles existant\n")
                    allConsole()
                    console_id = input("\nNouvelle console de ce jeu "
                                       "(Tapez l'id de la console parmi celles affichées): ")

                    updateGame(__id, name, description, console_id)

                    print("\nMise à jour effectuée avec succes")

                except:
                    print("""\n--- Soit les données du jeu sont erronés, dans ce cas,
                          veuillez réessayer avec des données valides.\n"
                          --- Soit ce jeu n'existe pas.
                          Veuillez indiquer l'id d'un jeu parmi les jeux afficher""")

            # Delete one game
            elif mg == "4":
                print("\n------------- Supprimer un jeu -------------\n")

                print("\nListe des jeux existant\n")
                allgames()

                try:
                    __id = input("\nL'id du jeu à supprimer: ")
                    deleteGame(__id)
                    print("\nLe jeu a bien été supprimé ")

                except:
                    print("\nCe jeu n'existe pas."
                          "Veuillez indiquer l'id d'un jeu parmi les jeux afficher")

            # Search a game
            elif mg == "5":
                print("\n------------- Chercher un jeu -------------\n")

                name = input("\nEntrer le nom du jeu que vous recherchez: ")
                try:
                    game = searchGame(name)
                    print("\nRésultat de la recherche: ")
                    print("""
                            Nom : {}
                            Description: {}
                            Console: {}""".format(game.name, game.description, game.console.name))

                except:
                    print("\nCe jeu n'existe pas."
                          "Veuillez réessayer: ")

            # back
            elif mg == "6":
                break

            else:
                print("\nCette commande n'exite pas. Veuillez réessayer avec une commande valide")

    # Quit
    elif mp == "3":
        print("\nMerci et à bientôt :)")
        exit()

    else:
        print("\nCette commande n'exite pas. Veuillez réessayer avec une commande valide")
