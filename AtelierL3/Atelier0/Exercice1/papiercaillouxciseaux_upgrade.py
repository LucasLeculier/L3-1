import random

# On definit les forces des 4 types de choix
beat_dict = {
    "pierre": ["ciseaux"],
    "papier":["pierre", "puit"],
    "ciseaux": ["papier"],
    "puit": ["pierre", "ciseaux"]
}

# Liste des choix possibles à jouer
list_choices = ["pierre", "papier", "ciseaux", "puit"]

game_type = ""

def init_game():

    choice = input("\n\nVoulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? : \n" )

    player_one_name = ""
    player_two_name = ""

    while True:
        if choice == 'O' :
            player_one_name = input("Quel est votre nom ? : \n")
            print("Bienvenue ", player_one_name, " nous allons jouer ensemble. \n")
            player_two_name = 'Machine'
            break

        elif choice == 'N' :
            player_one_name = input("Quel est votre nom ? : \n")
            print("Bienvenue ", player_one_name, " nous allons jouer ensemble. \n")
            player_two_name = input("Quel est le nom du deuxième joueur ? : \n")
            print("Bienvenue ", player_two_name, " nous allons jouer ensemble. \n")
            break

        else:
            print("Je n'ai pas compris votre réponse")
            choice = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? : \n" )

    return choice, player_one_name, player_two_name

# Returns True if the choice exists
def player_choice(choice):

    return choice in list_choices

# Game loop function
def main_game_loop():

    game = init_game()
    game_type = game[0]
    player_one_name = game[1]
    player_two_name = game[2]

    choice_player_one = ""
    choice_player_two = ""

    score_player_one = 0
    score_player_two = 0
    
    games_counter = 0

    should_continue = True

    while should_continue == True:  
        games_counter += 1 

        # Choix joueur 1
        choice_player_one = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=player_one_name))
        
        choice_player_oneok = player_choice(choice_player_one)
        while not choice_player_oneok:
            print("Je n'ai pas compris votre réponse.")
            choice_player_one = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=player_one_name))
            choice_player_oneok = player_choice(choice_player_one)

        # Choix Machine (non-joueur)
        if game_type == 'O': 
            choice_player_two = ['papier','pierre','ciseaux', 'puit'][random.randint(0, 3)]

        # Choix joueur 2
        else:
            choice_player_two = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=player_two_name))
        
            choice_player_twook = player_choice(choice_player_two)
            while not choice_player_twook:
                print("Je n'ai pas compris votre réponse.")
                choice_player_two = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=player_two_name))
                choice_player_twook = player_choice(choice_player_two)

        #On affiche les choix de chacun
        print("Choix des joueurs : ", player_one_name, f"a choisi [{choice_player_one}]", " | ", player_two_name, f"a choisi [{choice_player_two}]", "\n")


        # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
        winner = ""
        for e, bat in beat_dict.items():

            if choice_player_two != choice_player_one:

                if choice_player_one == e and choice_player_two in bat:
                    winner = player_one_name
                    score_player_one += 1
                    print(f"Le gagnant est {winner} !\n")
                    break
                elif choice_player_one == e and choice_player_two not in bat:
                    print("this else")
                    winner = player_two_name
                    score_player_two += 1
                    print(f"Le gagnant est {winner} !\n")
                    break

            else:
                print("Vous êtes ex æquo !")
                break
        
        print(f"Les scores a l'issue de cette manche : {player_one_name} [{score_player_one}] points | {player_two_name} [{score_player_two}] points.")

        # On demande a l'utilisateur s'il souhaite continuer de jouer tant que l'on a pas atteint le maximum de parties pouvant etre jouées 
        if games_counter < 5:
            # On propose de continuer ou de s'arrêter 
            continue_choice = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(player_one_name, player_two_name))
            if continue_choice == 'O':
                should_continue = True

            elif continue_choice == 'N':
                should_continue = False

            else:
                should_continue = True
                print("Vous ne répondez pas à la question, on continue...")
        else:
            should_continue = False

        print(f"Parties jouées {games_counter}")

    game_winner = player_one_name if score_player_one > score_player_two else player_two_name
    print(f"Le gagnant de ce match de pierre papier ciseaux est {game_winner} ! \n")
    print("Merci d'avoir joué ! A bientôt ! \n")


# Function calls
main_game_loop()