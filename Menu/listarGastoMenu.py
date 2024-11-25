
def listarGasto():
    while True:
        try:
            print(''''
    =============================================
                Storaged Expenses
    =============================================
    Choose an option to filter the storaged expenses:

    1. Show all expenses
    2. Filter by category
    3. Filter by date range
    4. Go back to the main menu
    =============================================
            ''')
            options = int(input('Please choose an option(1-4): '))
            if (options >= 1 and options <= 3):
                return options
            elif options == 4:
                break
            else: raise ValueError()
        
        except ValueError as e:
            print("\nInvalid option. Please choose a number between 1 and 4.")