# Lemonade change problem

def lemonadeChange(bills):  # Function to check whether you can provide the change
    
    change = []   # Empty list to collect change
    Check_change = True
    
    for i in bills:
        
        if i == 5:
            change.append(i)

        elif i == 10:
            if 5 not in change:
                Check_change = False
                break
            change.append(i)
            change.remove(5)

        elif i == 20:
            if 10 and 5 not in change:
                Check_change = False
                break
            change.append(i)
            change.remove(5)
            change.remove(10)

    return Check_change

class PriceError(Exception):  # creating PriceError and thereby ensures the valid price values to 5,10,20
    pass

n = int(input('\nEnter the number of bills: '))

bills = []  # Empty list to add the bills

for i in range(n):
    try:
        bill = int(input(f'\nEnter the bill amount({i + 1}): '))
        if bill != 5 and bill != 10 and bill != 20:  # Condition for PriceError
            raise PriceError
    except ValueError:  # Handling Non-integer value errors
        bill = int(input('\nEnter a valid number : '))
    except Exception as PriceError:  # Handling Price errors
        bill = int(input('\nEnter either 5, 10, 20 : '))
    finally:
        bills.append(bill)  # Adding the bills to the list

print(lemonadeChange(bills))  # Returns true if you can provide the correct change, else false