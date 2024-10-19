# Cameron Seaman
# game.py

import gamefunctions

# Test the imported code
username = input("Enter your name: ")
gamefunctions.print_welcome(username)
print('Here is the shop menu:')
monster = gamefunctions.random_monster()
gamefunctions.print_shop_menu('Sword', 25, 'Shield', 15)
print(f'You have ${monster["money"]} remaining.')
toBuy = int(input("Enter the number of swords you would like to buy: "))
amountPurchased, monster['money'] = gamefunctions.purchase_item(25, monster['money'], toBuy)
print(f'You purchased {amountPurchased} swords and have ${monster["money"]} remaining.')