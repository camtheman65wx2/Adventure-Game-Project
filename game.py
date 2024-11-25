# Cameron Seaman
# game.py

import gamefunctions
import gameGraphics

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
    print('Press \'m\' to access the game menu.')
    print('Press \'q\' to quit the game.')
    print()
    running = True
    enemies = [gameGraphics.WanderingMonster()]
    while running:
        option, enemy = gameGraphics.main(enemies)
        if option == 'm':
            gameGraphics.running = False
            consoleoption = gamefunctions.print_user_menu(username, monster)
            while consoleoption != '5':
                if consoleoption == '1':
                    monster = gamefunctions.sleep(monster)
                elif consoleoption == '2':
                    monster = gamefunctions.shop_menu(monster)
                elif consoleoption == '3':
                    gamefunctions.view_inventory(monster)
                elif consoleoption == '4':
                    gamefunctions.save_game(monster, username)
                elif consoleoption == '0':
                    print('Returning to game...')
                    print()
                    gameGraphics.running = True
                    break
                else:
                    print('Invalid option. Please try again.')
                consoleoption = gamefunctions.print_user_menu(username, monster)
            if consoleoption == '5':
                save = input('Would you like to save your game before quitting? (y/n): ')
                if save == 'y':
                    gamefunctions.save_game(monster, username)
                running = False
        elif option == 'f':
            monster, enemy.data = gamefunctions.fight_monster(monster, enemy.data)
            if enemy.data['health'] <= 0:
                enemies = [monster for monster in enemies if id(monster) != id(enemy)]
            if len(enemies) == 0:
                enemies.append(gameGraphics.WanderingMonster())
                enemies.append(gameGraphics.WanderingMonster())

if __name__ == '__main__':
    game()