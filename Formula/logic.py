import json
from tabulate import tabulate
from datetime import datetime, timedelta
import calendar

def read_file(path):
        with open(f'Server/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'Server/{path}', 'w') as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)
        file.close()

def storage(expense, category, date, description):
    data = read_file('storagedData.json')
    formato = {
         "Expense": expense,
         "Category": category,
         "Date": date,
         "Description": description
    }
    data.append(formato)
    write_file(data, 'storagedData.json')
    return data

# Load json data adaptaded to use tabulate
def listar():
    with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    titles = ["Expenses", "Category", "Date", "Description"]
    chart = [list(dato.values()) for dato in datos]
    result = print(tabulate(chart, headers=titles, tablefmt="grid"))
    return result
# The data we are getting from is a dictionary, so with "list(dato.values())" we make that dictionary a list to work with
# in a easier way. ablefmt = "grid" is the chart style 


# First we have to load the information, then we request to the user which category it want to filter.
# so that, we create a new list to save any match. For that we have to review all the information with
# for. If there's any match it will append it to the new list. At the end we reutilize the previous code
# for the new chart.

def categoryFilter():
    categoryOptions = ["basics bills", "food", "transportation", "entertainment", "others"]
    try:
        with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        category = input("Please type the category you want to filter: ").lower()
        if category in categoryOptions:
            pass
        else:
            raise ValueError()
        
        filtered = []

        for dato in datos:
            if dato["Category"].lower() == category:
                filtered.append(dato)
        
        if filtered:
            titles = ["Expenses", "Category", "Date", "Description"]
            chart = [list(dato.values()) for dato in filtered]
            result = print(tabulate(chart, headers=titles, tablefmt="grid"))
            return result
        else:
            print(f"\nThere's no any data for {category} category.")
    except ValueError as e:
        print("\nDear user, please type one of the listed categories.")

# We can reutilize the previous code because this filter only changes the data to compare with.
# Also, we have to use the library datetime to validate if the entered date is correct and also in the order we requested it.
def dateFilter():
    try:
        with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        date = input("Please type the beginning date you want to filter(YYYY/MM/DD): ")
        dateTwo = input("Please type the end date you want to filter(YYYY/MM/DD): ")
        validaD = datetime.strptime(date, "%Y/%m/%d")
        validaDt = datetime.strptime(dateTwo, "%Y/%m/%d")
        if not validaD and validaDt:
            raise ValueError()
        
        filtered = []

        for dato in datos:
            if date <= dato["Date"] <= dateTwo:
                filtered.append(dato)
        
        if filtered:
            titles = ["Expenses", "Category", "Date", "Description"]
            chart = [list(dato.values()) for dato in filtered]
            result = print(tabulate(chart, headers=titles, tablefmt="grid"))
            return result
        else:
            print(f"\nThere's no any data for {date} date filter.")
    except ValueError as e:
        print("\nDear user, please type a correct date or format date (YYYY/MM/DD).")


def calculateDailyTotal():
    try:
        with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        date = input("Please type the date you want to filter(YYYY/MM/DD): ")
        validaD = datetime.strptime(date, "%Y/%m/%d")
        if not validaD:
            raise ValueError()
        
        filtered = []

        for dato in datos:
            if dato["Date"] == date:
                filtered.append(dato)
        
        if filtered:
            total = 0
            for dato in filtered:
                total += dato["Expense"]
            result = print(f"\nThe total amount for the day {date} is: ${total}")
            return result
        
        else:
            print(f"\nThere's no any data for {date} date filter.")
    except ValueError as e:
        print("\nDear user, please type a correct date or format date (YYYY/MM/DD).")


def calculateWeeklyTotal():
    try:
        with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        date = input("Please type the beggining week date you want to filter(YYYY/MM/DD): ")
        validaD = datetime.strptime(date, "%Y/%m/%d")
        weekStart = validaD - timedelta(days=validaD.weekday())
        weekEnd = weekStart + timedelta(days=6)
        if not validaD:
            raise ValueError()
        
        filtered = []

        for dato in datos:
            if weekStart <= datetime.strptime(dato["Date"], "%Y/%m/%d") <= weekEnd:
                filtered.append(dato)
        
        if filtered:
            total = 0
            for dato in filtered:
                total += dato["Expense"]
            result = print(f"\nThe total amount for this week between {weekStart} and {weekEnd} was: ${total}")
            return result
        
        else:
            print(f"\nThere's no any data for {date} date filter.")
    except ValueError as e:
        print("\nDear user, please type a correct date or format date (YYYY/MM/DD).")

      
def calculateMonthlyTotal():
    try:
        with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        date = input("Please type a date you want to filter(YYYY/MM/DD): ")
        validaD = datetime.strptime(date, "%Y/%m/%d")
        monthStarted = validaD.replace(day=1)
        _, lastDay = calendar.monthrange(validaD.year, validaD.month)
        monthEnd = monthStarted.replace(day=lastDay)
        
        if not validaD:
            raise ValueError()
        
        filtered = []

        for dato in datos:
            if monthStarted <= datetime.strptime(dato["Date"], "%Y/%m/%d") <= monthEnd:
                filtered.append(dato)
        
        if filtered:
            total = 0
            for dato in filtered:
                total += dato["Expense"]
            result = print(f"\nThe total amount for this month bwtween {monthStarted} and {monthEnd} is: ${total}")
            return result
        
        else:
            print(f"\nThere's no any data for {date} date filter.")
    except ValueError as e:
        print("\nDear user, please type a correct date or format date (YYYY/MM/DD).")


def dailyReport():
        with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        date = datetime.now().date()
        formato = date.strftime("%Y/%m/%d")
        
        filtered = []
        total = 0

        for dato in datos:
            if dato["Date"] == formato:
                filtered.append(dato)
        
        if filtered:
            titles = ["Expenses", "Category", "Date", "Description"]
            chart = [list(dato.values()) for dato in filtered]
            for dato in filtered:
                total += dato["Expense"]
            resultThree = print(filtered)
            result = print(tabulate(chart, headers=titles, tablefmt="grid"))
            resultTwo = print(f"\nThe total amount for today is: ${total}")
            return result, resultTwo, resultThree


def storageDReport():
    with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    date = datetime.now().date()
    formato = date.strftime("%Y/%m/%d")

    data = read_file('dailyReports.json')
    filtered = []

    for dato in datos:
            if dato["Date"] == formato:
                filtered.append(dato)

    chart = [list(dato.values()) for dato in filtered]

    formatoD = {
        "Report": chart,
        "Description": f"This is the report for {formato} date."
        }
    data.append(formatoD)
    write_file(data, 'dailyReports.json')
    return data


def weeklyReport():
    with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        
    date = datetime.now().date()
    previousWeek = date - timedelta(weeks=1)
    weekStart = previousWeek - timedelta(days=previousWeek.weekday())
    weekEnd = weekStart + timedelta(days=6)
        
    filtered = []
    total = 0

    for dato in datos:
        formatoFecha = datetime.strptime(dato["Date"], "%Y/%m/%d").date()
        if weekStart <= formatoFecha <= weekEnd:
                filtered.append(dato)
        
    if filtered:
        titles = ["Expenses", "Category", "Date", "Description"]
        chart = [list(dato.values()) for dato in filtered]
        for dato in filtered:
            total += dato["Expense"]
        result = print(tabulate(chart, headers=titles, tablefmt="grid"))
        resultTwo = print(f"\nThe total amount for this week {date} is: ${total}")
        return result, resultTwo
        
def storageWReport():
    with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    date = datetime.now().date()
    previousWeek = date - timedelta(weeks=1)
    weekStart = previousWeek - timedelta(days=previousWeek.weekday())
    weekEnd = weekStart + timedelta(days=6)

    data = read_file('weeklyReports.json')
    filtered = []

    for dato in datos:
        formatoFecha = datetime.strptime(dato["Date"], "%Y/%m/%d").date()
        if weekStart <= formatoFecha <= weekEnd:
            filtered.append(dato)

    chart = [list(dato.values()) for dato in filtered]

    formatoD = {
        "Report": chart,
        "Description": f"This is the report for the week between {weekStart} and {weekEnd}."
        }
    data.append(formatoD)
    write_file(data, 'weeklyReports.json')
    return data

def monthlyReport():
    with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        
        date = datetime.now().date()
        monthStarted = date.replace(day=1)
        monthEnd = monthStarted - timedelta(days=1)
        previousMonthStarted = monthEnd.replace(day=1)
        
        filtered = []
        total = 0
        for dato in datos:
            formatoFecha = datetime.strptime(dato["Date"], "%Y/%m/%d").date()
            if previousMonthStarted <= formatoFecha <= monthEnd:
                filtered.append(dato)

    if filtered:
        titles = ["Expenses", "Category", "Date", "Description"]
        chart = [list(dato.values()) for dato in filtered]
        for dato in filtered:
            total += dato["Expense"]
        result = print(tabulate(chart, headers=titles, tablefmt="grid"))
        resultTwo = print(f"\nThe total amount for this month between {previousMonthStarted} and {monthEnd} is: ${total}")
        return result, resultTwo
    
def storageMReport():
    with open("Server/storagedData.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        
    date = datetime.now().date()

    date = datetime.now().date()
    monthStarted = date.replace(day=1)
    monthEnd = monthStarted - timedelta(days=1)
    previousMonthStarted = monthEnd.replace(day=1)

    data = read_file('monthlyReports.json')
    filtered = []

    for dato in datos:
        formatoFecha = datetime.strptime(dato["Date"], "%Y/%m/%d").date()
        if previousMonthStarted <= formatoFecha <= monthEnd:
            filtered.append(dato)

    chart = [list(dato.values()) for dato in filtered]

    formatoD = {
        "Report": chart,
        "Description": f"This is the report for this week between {monthStarted} and {monthEnd}."
        }
    data.append(formatoD)
    write_file(data, 'monthlyReports.json')
    return data