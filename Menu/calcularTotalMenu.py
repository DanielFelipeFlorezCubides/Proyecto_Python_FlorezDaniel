from Menu.mainMenu import mainMenu
def calculateTotal():
    while True:
        try:
            print('''
    =============================================
            Total ammount calculation
    =============================================
    Select which calculation you want to do:

    1. Calculate daily expenses
    2. Calculate weekly expenses
    3. Calculate monthly expenses
    4. Go back to the main menu
    =============================================''')
            
            options = int(input('Please choose an option(1-4): '))
            if (options >= 1 and options <= 3):
                return options
            elif options == 4:
                break
            else: raise ValueError()
        
        except ValueError as e:
            print("Invalid option. Please choose a number between 1 and 4.")