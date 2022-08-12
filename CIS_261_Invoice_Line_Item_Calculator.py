#David Prato CIS276 LABWK6 Invoice Calculator

def price_input(): #step 1- user price input.
    try: # try seems to be a good way to validate input data as the assigment requests to be done
        price= float(input("Enter Price: "))
        return price
    except ValueError:# if the user doesn't input a float
        print("Must be a decimal number, try again.")
        return price_input() #restarts the function


def quantity_input(): #step 2- user quantity input.
    try:
        quant = int(input("Enter Quantity: "))
        return quant
    except ValueError:
        print("Must be a whole number only, try again")
        return quantity_input()


#Main Program-------------------------------------------------
print("The Invoice Line Item Calculator")
cont = ""

while cont.lower() != 'n': # creating the loop iteration until no is selected
    print()
    price = price_input()
    quant = quantity_input()
    total = price * quant
    print()

    print(f'PRICE:{price:>10.2f}') #>11 gives us 11 spaces right justification, 2f gives us 0.00
    print(f'QUANTITY:{quant:>4}') #>4 4 spaces to the right indentation
    print(f'TOTAL{total:>12.2f}')

    cont = input("Would you like to make another line item selection? Type 'y' or 'n': ")

print("bye!")