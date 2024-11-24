import json

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