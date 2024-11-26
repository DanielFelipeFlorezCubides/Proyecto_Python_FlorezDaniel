from Formula.logic import monthlyReport, storageMReport
import os
def monthlyReportMenu():
    while True:
        try:
            print('''
    =============================================
                Generating reports
    =============================================
    Select report option:

    1. Show monthly report
    2. Storage report
    3. Go back to main menu
    =============================================''')
            
            options = int(input('Please choose an option(1-3): '))
            if (options == 1):
                monthlyReport()
            elif (options == 2):
                storageMReport()
                print('Report successfully saved!')
            elif (options == 3):
                os.system("Clear")
                break
            else: 
                raise ValueError()
        
        except ValueError as e:
            print("\nInvalid option. Please choose a number between 1 and 3.")