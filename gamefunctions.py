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

# Define random_monster function
def random_monster():
    """
    Generate a random monster with a name, description, health, power, and money.

    Parameters:
    None

    Returns:
    A dictionary containing the monster's name, description, health, power, and money.
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
    myMonster = {'name': name,'description': description, 'health': health, 'power': power, 'money': money}
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
    """
    string_to_print = f'Hello, {name}!'
    print(f'{string_to_print:^{width}}')

# Define print_shop_menu function
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
    # Proof of code functionality for print_shop_menu function
    print_shop_menu('Egg', 1, 'Pear', 12.34)
    print_shop_menu('Apple', 1.23, 'Banana', 0.23)
    print_shop_menu('Orange', 2.23, 'Grape', 3.23456)
# End of Program