import time


# Function that displays the Inventory
def displayInventory():
    print("%-7s %-30s %-10s %s" % ('Code:', 'Item:', 'Stock:', 'Sales:'))
    print("%-7s %-30s %-10s %s" % ('-----', '-----', '------', '------'))
    i = 0
    while i < (len(inventory)):
        print("%-7s %-30s %-10s %s" % (inventory[i][0], inventory[i][1], \
                                       inventory[i][2], inventory[i][3]))
        i += 1


# Function that does a linear search 
def linearSearch(itemCode):
    i = 0
    while i < (len(inventory)):
        if inventory[i][0] == itemCode.upper():
            return True, i
        i += 1
    else:
        return False, ''


# Function that displays the Main Menu
def menu():
    print('1.   List your current Inventory')
    print('2.   add New item')
    print('3.   receive the details of an item')
    print('4.   remove item')
    print('5.   edit item')
    print('6.   receive stock')
    print('7.   sale of product')
    print('8.   search product using name')
    print('9.   save the current inventory')
    print('Q.   (q)uit the program and save changes')
    print('\n')
    entry = input(str('Please enter one of the options above and "Q" to '
                      'save and quit: '))
    return entry.upper()


# Function that finds the details of an item
def findDetails():
    itemCode = input('Enter Item code for Search: ')
    check, i = linearSearch(itemCode)
    if check == True:
        code = inventory[i][0]
        name = inventory[i][1]
        stock = inventory[i][2]
        sales = inventory[i][3]
        return code, name, stock, sales
    else:
        print('\n')
        print('Item has not been found')
        print('\n')
        return '', '', '', ''


# Function that Adds an item to the list
def addItem():
    itemCode = input('Enter a 4 digit Alphanumeric Item Code: ').replace(" ", "")
    check, i = linearSearch(itemCode)
    if check == False:
        if len(itemCode) == 4:
            name = input('Enter Item Name: ')
            stock = input('Enter the total Stock Value: ')
            newItem = []
            newItem.append(itemCode.upper())
            newItem.append(name.title().replace(" ", ""))
            newItem.append(stock)
            newItem.append(0)
            inventory.append(newItem)
            print('\n')
            print('item has been added!')
            print('\n')
        else:
            print('\n')
            print('Item code must be 4 characters long!')
            print('\n')
    else:
        print('\n')
        print('Item Code already exists')
        print('\n')


# Function that Deletes an item from the list
def delItem():
    itemCode = input('Enter Item Code to delete: ')
    check, i = linearSearch(itemCode)
    if check == True:
        itemName = inventory[i][1]
        del (inventory[i])
        return itemName
    elif check == False:
        print('\n')
        print('The Item has Not been Found')
        print('\n')


# Function that edits a certain item
def editItem():
    itemCode = input('Enter Item code for Editing: ')
    check, i = linearSearch(itemCode)
    if check == True:
        editWhat = input('what would you like to edit(code,name,stock,sale): ').lower()
        if editWhat == 'code':
            newCode = input('enter a new 4 digit alphanumeric code: ').upper()
            del (inventory[i][0])
            inventory[i].insert(0, newCode)
        elif editWhat == 'name':
            newName = input('what would you like to change the name to: ')
            del (inventory[i][1])
            inventory[i].insert(1, newName.title().replace(" ", ""))
            print('\n')
        elif editWhat == 'stock':
            newStock = input('what would you like to change the stock to: ')
            del (inventory[i][2])
            inventory[i].insert(2, newStock)
            print('\n')
        elif editWhat == 'sale':
            newSale = input('what would you like to change the sales to: ')
            del (inventory[i][3])
            inventory[i].insert(3, newSale)
            print('\n')
        else:
            print('\n')
            print('You can not change the', editWhat, 'please try again!')
            print('\n')
    elif check == False:
        print('\n')
        print('The Item has Not been Found')
        print('\n')


# Function that adds stock of an item
def addStock():
    itemCode = input('Enter Item Code to add Stock value: ')
    check, i = linearSearch(itemCode)
    if check == True:
        stock = int(input('how much stock will you like to add? '))
        (inventory[i][2])
        newStock = int(inventory[i][2]) + stock
        del (inventory[i][2])
        inventory[i].insert(2, newStock)
        print('Great! you now have', newStock, 'in stock!')
        print('\n')
    else:
        print('\n')
        print('The Item has Not been Found')
        print('\n')


# Funtion that adds number of sales to an item
def addSales():
    itemCode = input('Enter Item code to add number of products sold: ')
    check, i = linearSearch(itemCode)
    if check == True:
        sales = int(input('how much sales will you like to add? '))
        (inventory[i][3])
        newSales = int(inventory[i][3]) + sales
        del (inventory[i][3])
        inventory[i].insert(3, newSales)
        print('Great! you now have sold', newSales, 'items')
        print('\n')
    else:
        print('\n')
        print('The Item has Not been Found')
        print('\n')


def searchItem():
    itemName = input('please enter the item name: ').lower().replace(' ', '')
    i = 0
    while i < (len(inventory)):
        if inventory[i][1].lower() == itemName:
            code = inventory[i][0]
            name = inventory[i][1]
            stock = inventory[i][2]
            sales = inventory[i][3]
            return code, name, stock, sales
        i += 1
    print('\n')
    print('Item has not been found')
    print('\n')
    return '', '', '', ''


# Function that saves the program
def saveInventory():
    with open('myInventory.txt', 'w') as file:
        i = 0
        while i < (len(inventory)):
            file.write(str(inventory[i][0]))
            file.write(' ')
            file.write(str(inventory[i][1]))
            file.write(' ')
            file.write(str(inventory[i][2]))
            file.write(' ')
            file.write(str(inventory[i][3]))
            file.write('\n')
            i += 1

        # Main Program


# Intro to the program + importing all elements from the text file
print('\n')
print('Here is your Inventory:')
print('\n')

with open("myInventory.txt", 'r') as file:
    inventory = []
    for line in file:
        x = list(line.split())
        inventory.append(x)
        totalItems = len(inventory)

print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
print('▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓')
print('▓▓░▒▒░░░░░▒▒░▒▒▒▒▒░▒▒░░░░▒▒░░░░▒▒▒▒▒▒░░░▓▓')
print('▓▓░▒▒░░░░░▒▒░▒▒░░░░▒▒░░░░▒▒░░▒▒░░░░░░▒▒░▓▓')
print('▓▓░▒▒▒▒▒▒▒▒▒░▒▒▒▒▒░▒▒░░░░▒▒░░▒▒░░░░░░▒▒ ▓▓')
print('▓▓░▒▒░░░░░▒▒░▒▒▒▒▒░▒▒░░░░▒▒░░▒▒░░░░░░▒▒░▓▓')
print('▓▓░▒▒░░░░░▒▒░▒▒░░░░▒▒░░░░▒▒░░▒▒░░░░░░▒▒░▓▓')
print('▓▓░▒▒░░░░░▒▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒▒░░░▓▓')
print('▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓')
print('▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓')
print('▓▓░░░░▒▒░░░░░▒▒░▒▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓')
print('▓▓░░░░▒▒░░░░░▒▒░▒▒░░░░░▒▒░░░░▒▒░░▒▒░░░░░▓▓')
print('▓▓░░░░▒▒░░░░░▒▒░▒▒▒▒▒▒░▒▒▒▒░░▒▒▒▒░░░░░░░▓▓')
print('▓▓░░░░▒▒░░░░░▒▒░░░░░▒▒░▒▒░░░░▒▒░░▒▒░░░░░▓▓')
print('▓▓░░░░▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒░▒▒▒▒▒░▒▒░░▒▒░░░░░▓▓')
print('▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
print('_______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
print('______▒_______________▒▒▒▒▒▒▒▒')
print('_____▒________________▒▒▒▒▒▒▒▒')
print('____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
print('___▒')
print('__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
print('_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓')
print('▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓')
print('▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓')
print('▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
print('▒▒')

print('\n')
displayInventory()
print('\n' * 3)

entry = ''

while entry.upper() != 'Q':
    print('===================================')
    print('Here are your Option to chose from:')
    print('===================================')
    entry = menu()
    if entry == '1':
        print('\n')
        displayInventory()
        print('\n')
    elif entry == '2':
        addItem()
    elif entry == '3':
        code, name, stock, sales = findDetails()
        if code != '':
            print('\n')
            print('Here are the details for item', code)
            print('Item name:', name)
            print('Item stock/quantity:', stock)
            print('Item sales:', sales)
            print('\n')
            time.sleep(3)
    elif entry == '4':
        itemName = delItem()
        if itemName != None:
            print('\n')
            print('the item', itemName, 'has been deleted')
            print('\n')
    elif entry == '5':
        editItem()
    elif entry == '6':
        addStock()
    elif entry == '7':
        addSales()
    elif entry == '8':
        code, name, stock, sales = searchItem()
        if code != '':
            print('\n')
            print('Here are the details for item', code)
            print('Item name:', name)
            print('Item stock/quantity:', stock)
            print('Item sales:', sales)
            print('\n')
            time.sleep(3)
    elif entry == '9':
        saveInventory()
        print('Progress Saved!')
        print('\n')
    elif entry == 'Q':
        ''
    else:
        print('\n')
        print('unknown entry, please try again')
        print('\n')

saveInventory()
print('\n')
print('Your last entries have been auto saved')
