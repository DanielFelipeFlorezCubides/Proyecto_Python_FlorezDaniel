import os
def mainMenu():
    while True:
        try:
            print('''
    =============================================
                Expenses contability
    =============================================
    Options to choose from:

    1. Storage a new expense
    2. Show storaged expenses
    3. Calculate the total amount
    4. Generate a report
    5. Exit
    =============================================
            ''')
            options = int(input('Please choose an option(1-5): '))
            if (options >= 1 and options <= 4):
                return options
            elif options == 5:
                    decission = int(input('Are you sure you want to leave?(1 = yes, 0 = no): '))
                    if decission == 1:
                        print(''' 
    ========================================
    Thank you for using Expenses contabiliy!
    ========================================
                              ''')
                        break
                    elif decission == 0:
                        print('ok')
                        os.system('clear')
            else: raise ValueError()
        
        except ValueError as e:
            print("Invalid option. Please choose a number between 1 and 5.")