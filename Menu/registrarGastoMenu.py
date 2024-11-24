from Menu.mainMenu import mainMenu
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
                category = input('ex. food, transportation, entertainment, others: ')
                date = input('format (YYYY/MM/DD): ')
                Description = input('Please type a short description of the expense: ')
                print('''
    =============================================
                      ''')
                
                option = int(input("Type '1' to save or '0' to cancel."))
                if option == 1:
                    print('Expense saved successfully!')
                elif option == 0:
                    print('Operation cancelled.')
                    break
            
            except Exception as e:
                print('Dear user, please type a correct ammount for the expense')