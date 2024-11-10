"""Functions for the game, including purchasing items, generating random monsters, and printing messages.

This module provides several functions to support the adventure game. These functions include purchasing items, generating random monsters, and printing welcome messages and shop menus.

Functions:
  - purchase_item: Purchase as many items as possible with the starting money, given the item price and quantity to purchase.
  - random_monster: Generate a random monster with a name, description, health, power, and money.
  - print_welcome: Print a centered welcome message using the provided name and width.
  - print_shop_menu: Print a formatted shop menu using the provided item names and prices.

Typical usage example:

  quantityPurchased, remainingMoney = purchase_item(10, 100, 5)
  myMonster = random_monster()
  print_welcome('Cameron')
  print_shop_menu('Egg', 1, 'Pear', 12.34)
"""

# Import the random module for the random_monster function
import random
import time
import math
import json
import os

def save_game(monster, username):
    """
    Save the game state to a JSON file for use in future game sessions.

    Parameters:
    monster (dict): The dictionary containing the monster's information
    username (str): The name of the user playing the game

    Returns:
    None
    """
    filename = 'game_save_data.json'
    game_data = {
        'username': username,
        'monster': monster
    }
    with open(filename, 'w') as file:
        json.dump(game_data, file, indent=4)
        file.flush()
    print('Game saved successfully.')

def load_game():
    """
    Load the game state from a JSON file.

    Parameters:
    username (str): The name of the user playing the game

    Returns:
    The dictionary containing the monster's information and username if the game was loaded successfully, otherwise None
    """
    filename = 'game_save_data.json'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            game_data = json.load(file)
            monster = game_data['monster']
            username = game_data['username']
            print('Game loaded successfully.')
            time.sleep(1)
            return monster, username
    else:
        return None, None

def pregame_menu():
    """
    Display the pregame menu for the game, allowing the user to start a new game or load a saved game.

    Parameters:
    None

    Returns:
    The user's choice for starting a new game or loading a saved game
    """
    print('Welcome to the adventure game!')
    print()
    print('1) Start New Game')
    print('2) Load Saved Game')
    print()
    choice = input('Enter your choice: ')
    return choice

# Define purchase_item function
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """
    Purchase as many items as possible with the starting money, given the item price and quantity to purchase.

    Parameters:
    itemPrice (float): The price of a single item.
    startingMoney (float): The amount of money available to spend.
    quantityToPurchase (int, optional): The number of items to purchase. Default is 1.

    Returns:
    The number of items purchased and the remaining money after the purchase.

    Example:
    purchase_item(10, 100, 5)
    """
    # Find if the wanted quantity is more than what is affordable, if it is, buy as much as they can afford
    if itemPrice * quantityToPurchase > startingMoney:
        quantityToPurchase = startingMoney // itemPrice
        remainingMoney = startingMoney - (itemPrice * quantityToPurchase)
        quantityPurchased = quantityToPurchase
    else:
        quantityPurchased = quantityToPurchase
        remainingMoney = startingMoney - (itemPrice * quantityToPurchase)
    return quantityPurchased, remainingMoney

def add_item_to_inventory(inventory, item):
    """
    Add an item to the inventory list.

    Parameters:
    inventory (list): The dictionary of items in the inventory.
    item (dict): The item to add to the inventory.

    Returns:
    The updated inventory list with the new item added.

    Example:
    monster["inventory"] = add_item_to_inventory(inventory, item)
    """
    inventory.append(item)
    return inventory

# Define random_monster function
def random_monster():
    """
    Generate a random monster with a name, description, health, power, and money.

    Parameters:
    None

    Returns:
    A dictionary containing the monster's name, description, health, power, and money, as well as base inventory.

    Example:
    monster = random_monster()
    """
    # Create a list of monster names and descriptions
    names = ['Goblin', 'Dragon', 'Ogre', 'Troll']
    descriptions = ['This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.', 'This is a mighty dragon. It soars above you, casting a shadow over the land before unleashing a torrent of flames.', 'This is a fearsome ogre. It lumbers towards you, its massive club swinging menacingly.', 'This is a menacing troll. It grunts and growls, brandishing a large, jagged rock.']
    # Randomly select a monster based by name in the list
    name = random.choice(names)
    # match the description based on the randomly selected name above
    description = descriptions[names.index(name)]
    # Randomly generate health, power, and money values based on the monster name with a range of acceptable values
    if name == 'Goblin':
        health = random.randint(10, 30)
        power = random.randint(5, 15)
        money = random.randint(1, 50)
    elif name == 'Dragon':
        health = random.randint(50, 100)
        power = random.randint(70, 80)
        money = random.randint(100, 1000)
    elif name == 'Ogre':
        health = random.randint(30, 60)
        power = random.randint(45, 60)
        money = random.randint(50, 200)
    elif name == 'Troll':
        health = random.randint(20, 50)
        power = random.randint(15, 30)
        money = random.randint(20, 100)
    # define the dictionary to return later
    myMonster = {'name': name,'description': description, 'health': health, 'power': power, 'money': money, 'inventory': []}
    return myMonster

# Define print_welcome function
def print_welcome(name, width=20):
    """
    Prints a centered welcome message using the provided name and width.

    Parameters:
    name (str): The name to include in the welcome message.
    width (int, optional): The total width of the printed message to center within. Default is 20.

    Returns:
    Nothing, but prints the welcome message.

    Example:
    print_welcome('Cameron')
    """
    string_to_print = f'Hello, {name}!'
    print(f'{string_to_print:^{width}}')

# Define shop_menu function
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Prints a formatted shop menu using the provided item names and prices.

    Parameters:
    item1Name (str): The name of the first item.
    item1Price (float): The price of the first item.
    item2Name (str): The name of the second item.
    item2Price (float): The price of the second item.

    Returns:
    None, but prints the shop menu.
    """
    price1 = f'${item1Price:.2f}'
    price2 = f'${item2Price:.2f}'
    print('/----------------------\\')
    print(f'| {item1Name:<12}{price1:>8} |')
    print(f'| {item2Name:<12}{price2:>8} |')
    print('\\----------------------/')



def shop_menu(monster):
    items = [
        {'name': 'Sword', 'type': 'weapon', 'price': 15, 'power': 10, 'maxDurability': 100, 'currentDurability': random.randint(30, 100)},
        {'name': 'Potion', 'type': 'consumable', 'price': 100},
    ]
    while True:
        print('/----------------------\\')
        for itemid, item in enumerate(items):
            price = f'${item["price"]:.2f}'
            print(f'| {itemid + 1}) {item["name"]:<9}{price:>8} |')
        print('\\----------------------/')
        print('0) Exit Shop')

        choice = input('Enter the number of the item you want to purchase (or 0 to exit shop): ')

        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(items):
            if choice == '0':
                print('Exiting shop...')
                time.sleep(1)
                print()
                print()
                return monster
            print('Invalid choice, please try again.')
            choice = input('Enter the number of the item you want to purchase (or 0 to exit shop): ')

        choice = int(choice) - 1
        if choice >= 0 and choice < len(items):
            item = items[choice]
            quantity = input(f'How many {item["name"]}s would you like to purchase? (or 0 to exit shop): ')
            if quantity.isdigit():
                if int(quantity) == 0:
                    print('Exiting shop...')
                    print()
                    time.sleep(1)
                    return monster
                quantity = int(quantity)
                quantityPurchased, remainingMoney = purchase_item(item['price'], monster['money'], quantity)
                if quantityPurchased > 0:
                    print('Purchasing...')
                    time.sleep(2)
                    monster['money'] = remainingMoney
                    for number in range(quantityPurchased):
                        monster['inventory'] = add_item_to_inventory(monster['inventory'], item.copy())
                    print(f'You purchased {quantityPurchased} {item["name"]}(s).')
                    print()
                    time.sleep(1)
                else:
                    print('You do not have enough money to make this purchase.')
                    time.sleep(1)
                    print()
                    print('Exiting shop...')
                    print()
                    time.sleep(1)
            else:
                print('Invalid input. Please enter a number.')
        else:
            print('Invalid choice. Please try again.')
        return monster

def print_user_menu(username, monster):
    """
    Print the user menu for the game, including the user's health and money. Allows the user to choose between fighting a monster, sleeping to restore health, or quitting the game.

    Parameters:
    username (str): The name of the user playing the game
    monster (dict): The dictionary containing the monster's health and money

    Returns:
    The user's choice for the game
    """
    print(f'Current HP: {monster["health"]}')
    print(f'Current Gold: {monster["money"]}')
    print(f'{username}, what would you like to do?')
    print()
    print('1) Fight Monster')
    print('2) Sleep (5 Gold, restores 10 HP)')
    print('3) Visit Shop')
    print('4) View Inventory')
    print()
    print('5) Save Game')
    print('6) Quit')
    print()
    option = input('Enter your choice: ')
    return option

def fight_monster(monster):
    """
    Fight the monster in the game. The player's health and money will be updated based on the outcome of the fight.

    Parameters:
    monster (dict): The dictionary containing the monster's health and power

    Returns:
    The updated monster dictionary after the fight
    """
    enemy = random_monster()
    print()
    print(f'A {enemy["name"]} appears!')
    print(f'{enemy["description"]}')
    print()
    print(f'Your HP: {monster["health"]}')
    print(f'Enemy HP: {enemy["health"]}')
    print()
    weapon_used = False

    while monster["health"] > 0 and enemy["health"] > 0:
        print('1) Attack')
        print('2) Run')
        print('3) Use Weapon')
        print('4) Use Consumable')
        choice = input('What\'s your next move: ')
        if choice == '1':
            base_damage = monster["power"]
            if weapon_used:
                base_damage += 20
                print('You swing your sword with increased power!')
                weapon_used = False
                damage_enemy = math.floor(base_damage * random.uniform(0.8, 1.2))
            else:
                damage_enemy = math.floor(base_damage * random.uniform(0.3, 0.8))
            print(f'You attack the enemy for {damage_enemy} damage!')
            enemy["health"] -= damage_enemy
            if enemy["health"] <= 0:
                enemy["health"] = 0
            print(f'Enemy HP: {enemy["health"]}')
            time.sleep(1)
            if enemy["health"] > 0:
                damage = math.floor(enemy["power"] * random.random())
                print(f'The enemy attacks you for {damage} damage!')
                time.sleep(1)
                monster["health"] -= damage
                if monster["health"] <= 0:
                    monster["health"] = 0
                print()
                print(f'Your HP: {monster["health"]}')
                print(f'Enemy HP: {enemy["health"]}')
                print()
        elif choice == '2':
            print('You run away!')
            print('You dropped some gold while running away.')
            monster["money"] -= random.randint(1, 10)
            if monster["money"] < 0:
                monster["money"] = 0
            return monster
        elif choice == '3':
            weapons = [item for item in monster["inventory"] if item["type"] == "weapon"]
            if weapons:
                print('Choose a weapon to use:')
                for idx, weapon in enumerate(weapons):
                    print(f'{idx + 1}) {weapon["name"]} (Durability: {weapon["currentDurability"]}/{weapon["maxDurability"]})')
                weapon_choice = input('Enter the number of the weapon you want to use: ')
                if weapon_choice.isdigit() and 1 <= int(weapon_choice) <= len(weapons):
                    weapon = weapons[int(weapon_choice) - 1]
                    print(f'You wield the {weapon["name"]} to increase your attack damage!')
                    weapon_used = True
                    weapon['currentDurability'] -= 10
                    if weapon['currentDurability'] <= 0:
                        print()
                        print(f'Your {weapon["name"]} will break after your next move!')
                        print()
                        monster["inventory"].remove(weapon)
                    else:
                        print(f'New Durability of {weapon["name"]}: {weapon["currentDurability"]}/{weapon["maxDurability"]}')
                else:
                    print('Invalid choice.')
            else:
                print('You have no weapon to use.')
        elif choice == '4':
            consumables = [item for item in monster["inventory"] if item["type"] == "consumable"]
            if consumables:
                print('Choose a consumable to use:')
                for idx, consumable in enumerate(consumables):
                    print(f'{idx + 1}) {consumable["name"]}')
                consumable_choice = input('Enter the number of the consumable you want to use: ')
                if consumable_choice.isdigit() and 1 <= int(consumable_choice) <= len(consumables):
                    if consumables[int(consumable_choice) - 1]["name"] == "Potion":
                        print('You used a Potion!')
                        print('This grants you the ability to defeat your enemy in one strike!')
                        print()
                        print('You attack the enemy for full damage!')
                        print()
                        time.sleep(1)
                        enemy["health"] = 0
                        monster["inventory"].remove(consumables[int(consumable_choice) - 1])
                    else:
                        print('This has not been implemented yet.')
                        # TODO: Implement other consumables as needed in future
                else:
                    print('Invalid choice.')
            else:
                print('You have no consumable to use.')

    if monster["health"] <= 0:
        print('You were defeated!')
        monster["money"] = monster["money"] // 2
        print('Respawning as a new monster...')
        time.sleep(2)
        monster = random_monster()
        print(f'You respawned as a {monster["name"]}')
    elif enemy["health"] <= 0:
        time.sleep(1)
        print()
        print('You defeated the enemy!')
        print('You gain some gold.')
        time.sleep(1)
        monster["money"] += enemy["money"]
    return monster

def sleep(monster):
    """
    Sleep in the game to restore health. The player's health and money will be updated based on the outcome of sleeping.

    Parameters:
    monster (dict): The dictionary containing the monster's health and money

    Returns:
    The updated monster dictionary after sleeping
    """
    if monster["money"] >= 5:
        print('You sleep and gain 10 HP.')
        monster["health"] += 10
        monster["money"] -= 5
        time.sleep(1)
    else:
        print('You do not have enough gold to sleep.')
    return monster

def view_inventory(monster):
    """
    View the inventory of the monster in the game.

    Parameters:
    monster (dict): The dictionary containing the monster's inventory

    Returns:
    None, but prints the items in the monster's inventory
    """
    print('Inventory:')
    if monster["inventory"]:
        for item in monster["inventory"]:
            if item["type"] == "weapon":
                # TODO: Add other weapon types as needed in future, similar to consumables
                print(f'{item["name"]} (Weapon) - Durability: {item["currentDurability"]}/{item["maxDurability"]} - Adds extra damage to attacks')
            elif item["type"] == "consumable":
                if item["name"] == "Potion":
                    print(f'{item["name"]} (Consumable) - Defeat your enemy in one strike.')
    else:
        print('Your inventory is empty.')
    print('Press any key to continue...')
    input()


if __name__ == '__main__':
    # Print proof of code functionality for purchase_item function
    quantityPurchased, remainingMoney = purchase_item(10, 100, 5)
    print(f'You purchased {quantityPurchased} items and have ${remainingMoney} left.')
    quantityPurchased, remainingMoney = purchase_item(10, 100, 12)
    print(f'You purchased {quantityPurchased} items and have ${remainingMoney} left.')
    quantityPurchased, remainingMoney = purchase_item(10, 100, 10)
    print(f'You purchased {quantityPurchased} items and have ${remainingMoney} left.')
    # Print proof of code functionality for random_monster function, printing 3 random monsters
    myMonster = random_monster()
    print('First Monster:')
    print(f"Name: {myMonster['name']}")
    print(f"Description: {myMonster['description']}")
    print(f"Health: {myMonster['health']}")
    print(f"Power: {myMonster['power']}")
    print(f"Money: {myMonster['money']}")

    myMonster = random_monster()
    print('Second Monster:')
    print(f"Name: {myMonster['name']}")
    print(f"Description: {myMonster['description']}")
    print(f"Health: {myMonster['health']}")
    print(f"Power: {myMonster['power']}")
    print(f"Money: {myMonster['money']}")

    myMonster = random_monster()
    print('Third Monster:')
    print(f"Name: {myMonster['name']}")
    print(f"Description: {myMonster['description']}")
    print(f"Health: {myMonster['health']}")
    print(f"Power: {myMonster['power']}")
    print(f"Money: {myMonster['money']}")
    # Proof of code functionality for print_welcome function
    print_welcome('Cameron')
    print_welcome('Cam')
    print_welcome('Lilly')
# End of Program