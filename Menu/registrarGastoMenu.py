from Formula.logic import storage
from datetime import datetime
# First we set a list with the possible options on the category section to not make the program more complex than it should be
categoryOptions = ["basics bills", "food", "transportation", "entertainment", "others"]

# Then we set the function in charge to display the menu to storage a new dictionary with the expense information
def registrarMenu():
    while True:
            print(f'''
    =============================================
                Storage a new expense
    =============================================
            Type expense's information
            ''')
            try:
                expenseAmmount = float(input('Please type the amount: '))
                if expenseAmmount <= 0:
                    raise ValueError()
                category = input("These are the categories: basics bills, food, transportation, entertainment, others. Please select one on the list: ").lower()
                date = input('format (YYYY/MM/DD): ')
                validaD = datetime.strptime(date, "%Y/%m/%d")
                description = input('Please type a short description of the expense: ')
                print('''
    =============================================
                      ''')
                if not validaD:
                     raise ValueError()
                
                if category in categoryOptions:
                     pass
                else:
                     raise ValueError()
                
                option = int(input("Type '1' to save or '0' to cancel: "))
                if (option == 1):
                    storage(expenseAmmount, category, date, description)
                    print('Expense successfully saved!')
                    break
                elif (option == 0):
                    print('Operation cancelled.')
                    break
            
            except ValueError as e:
                print('\nDear user, please type a correct ammount for the expense, one of the listed categories, or the correct format to type the date.')