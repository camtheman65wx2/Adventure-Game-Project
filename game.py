# Cameron Seaman
# game.py

import gamefunctions

def game():
    print('Welcome to the adventure game!')
    username = input('Enter your name to get started: ')
    monster = gamefunctions.random_monster()
    gamefunctions.print_welcome(username)
    print()
    option = gamefunctions.print_user_menu(username, monster)
    while option != '1' and option != '2' and option != '3':
        print('Invalid option. Please try again.')
        option = gamefunctions.print_user_menu(username, monster)
    while option == '1' or option == '2' or option == '3':
        if option == '1':
            monster = gamefunctions.fight_monster(monster)
            option = gamefunctions.print_user_menu(username, monster)
        elif option == '2':
            monster = gamefunctions.sleep(monster)
            option = gamefunctions.print_user_menu(username, monster)
        elif option == '3':
            print('Thanks for playing!')
            return

if __name__ == '__main__':
    game()