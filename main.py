from Menu.mainMenu import mainMenu
from Menu.registrarGastoMenu import registrarMenu
from Menu.listarGastoMenu import listarGasto
from Menu.generarReporteMenu import reportGenerator
from Menu.calcularTotalMenu import calculateTotal

while True:
    match mainMenu():
        case 1: registrarMenu()
        case 2: listarGasto()
        case 3: calculateTotal()
        case 4: reportGenerator()