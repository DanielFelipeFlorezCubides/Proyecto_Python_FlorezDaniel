from Formula.logic import weeklyReport ,storageWReport
import os
def weeklyReportMenu():
    while True:
        try:
            print('''
    =============================================
                Generating reports
    =============================================
    Select report option:

    1. Show weekly report
    2. Storage report
    3. Go back to main menu
    =============================================''')
            
            options = int(input('Please choose an option(1-3): '))
            if (options == 1):
                weeklyReport()
            elif (options == 2):
                storageWReport()
                print('Report successfully saved!')
            elif (options == 3):
                os.system("Clear")
                break
            else: 
                raise ValueError()
        
        except ValueError as e:
            print("\nInvalid option. Please choose a number between 1 and 3.")