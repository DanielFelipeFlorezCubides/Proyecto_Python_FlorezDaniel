from Menu.mainMenu import mainMenu
def reportGenerator():
    while True:
        try:
            print('''
    =============================================
                Generating reports
    =============================================
    Select report option:

    1. Daily report
    2. Weekly report
    3. Monthly report
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