# Cameron Seaman
# game.py

import gamefunctions

def game():
    preGameChoice = gamefunctions.pregame_menu()
    while preGameChoice != '1' and preGameChoice != '2':
        print('Invalid option. Please try again.')
        preGameChoice = gamefunctions.pregame_menu()
    if preGameChoice == '1':
        username = input('Enter your name to get started: ')
        monster = gamefunctions.random_monster()
        gamefunctions.print_welcome(username)
    elif preGameChoice == '2':
        monster, username = gamefunctions.load_game()
        if monster is None or username is None:
            print('No saved game found. Starting a new game.')
            username = input('Enter your name to get started: ')
            monster = gamefunctions.random_monster()
        gamefunctions.print_welcome(username)
    print()
    option = gamefunctions.print_user_menu(username, monster)
    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
        print('Invalid option. Please try again.')
        option = gamefunctions.print_user_menu(username, monster)
    while option != '6':
        if option == '1':
            monster = gamefunctions.fight_monster(monster)
            option = gamefunctions.print_user_menu(username, monster)
        elif option == '2':
            monster = gamefunctions.sleep(monster)
            option = gamefunctions.print_user_menu(username, monster)
        elif option == '3':
            monster = gamefunctions.shop_menu(monster)
            option = gamefunctions.print_user_menu(username, monster)
        elif option == '4':
            gamefunctions.view_inventory(monster)
            option = gamefunctions.print_user_menu(username, monster)
        elif option == '5':
            gamefunctions.save_game(monster, username)
            option = gamefunctions.print_user_menu(username, monster)
        else:
            print('Invalid option. Please try again.')
            option = gamefunctions.print_user_menu(username, monster)
    print('Goodbye! Thanks for playing!')

if __name__ == '__main__':
    game()