print('Welcome to the Jaxon Bozor')
print()

menu = ['Matiz', 'Damas', 'Nexia', 'Gentra', 'Tracker', 'Trailblazer', 'Equinox', 'Tahoe']
price = [3000,    6000,     6500,    9000,     12000,       14000,       27000,     60000]


print('ITEM', 'PRICE (INR), excl Tax', sep='\t\t\t')
for kk in range(len(menu)):
    print(str(kk+1) + '.' + menu[kk], price[kk], sep='\t\t')

print()

shopping_complete = 0

shopping_cart = []
shopping_quant = []


while shopping_complete == 0:
    order = int(input('Enter 1 to 8 to select a car item, 9 to proceed to checkout\n'))

    if order <= 8:
        print('User is shopping')
        print('You selected', menu[order-1])
        quant = int(input('How many units do you wish to purchase?\n'))

        if menu[order-1] in shopping_cart:
            print('Repeated selection')
            idx = shopping_cart.index(menu[order-1])
            print(idx)
            shopping_quant[idx] += quant


        else:
            print('New selection')
            shopping_cart.append(menu[order-1])
            shopping_quant.append(quant)


    elif order == 9:
        print('Proceeding to checkout')
        shopping_complete = 1
    else:
        print('Invalid Input')

print()
print('Shopping is complete, displaying shopping cart')

print()
print('ITEM', '\bQUANT', '\bUNIT PRICE', 'TOTAL', sep='\t\t\t')

grand_tot = 0.0

for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price = price[idx]
    tot_price = round(shopping_quant[kk]*unit_price, 2)
    grand_tot = grand_tot + tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')


print()

tax_rate = 6
tax = round(tax_rate/100.0*(grand_tot), 2)


print('Your total order value is', round(grand_tot, 2))
print('Tax (6%) is', tax)
print('Total ayou have to pay (IN US)', round(grand_tot+tax, 2))

print('Thanks')
print('See you next time')




