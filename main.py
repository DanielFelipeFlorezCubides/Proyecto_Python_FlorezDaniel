from Menu.mainMenu import mainMenu
from Menu.registrarGastoMenu import registrarMenu
from Menu.listarGastoMenu import listarGasto
from Menu.generarReporteMenu import reportGenerator
from Menu.calcularTotalMenu import calculateTotal
from Formula.logic import listar, categoryFilter, dateFilter

while True:
    match mainMenu():
        case 1: registrarMenu()
        case 2: 
            option = listarGasto()
            if (option == 1): listar()
            elif (option == 2): categoryFilter()
            elif (option == 3): dateFilter()
        case 3: calculateTotal()
        case 4: reportGenerator()
        case _: exit()