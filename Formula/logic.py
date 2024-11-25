import json
from tabulate import tabulate
from datetime import datetime

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
# Also, we have to use the library datetime to validate if the entered date is correct and in the order we requested it.
def dateFilter():
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
            titles = ["Expenses", "Category", "Date", "Description"]
            chart = [list(dato.values()) for dato in filtered]
            result = print(tabulate(chart, headers=titles, tablefmt="grid"))
            return result
        else:
            print(f"\nThere's no any data for {date} date filter.")
    except ValueError as e:
        print("\nDear user, please type a correct format fot the date (YYYY/MM/DD).")