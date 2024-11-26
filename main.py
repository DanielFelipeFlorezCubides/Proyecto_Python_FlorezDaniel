from Menu.mainMenu import mainMenu
from Menu.registrarGastoMenu import registrarMenu
from Menu.listarGastoMenu import listarGasto
from Menu.generarReporteMenu import reportGenerator
from Menu.calcularTotalMenu import calculateTotal
from Menu.reporteDiarioMenu import dailyReportMenu
from Menu.reporteSemanalMenu import weeklyReportMenu
from Menu.reporteMensualMenu import monthlyReportMenu
from Formula.logic import listar, categoryFilter, dateFilter, calculateDailyTotal, calculateWeeklyTotal, calculateMonthlyTotal

while True:
    match mainMenu():
        case 1: registrarMenu()
        case 2: 
            option = listarGasto()
            if (option == 1): listar()
            elif (option == 2): categoryFilter()
            elif (option == 3): dateFilter()
        case 3:
            option = calculateTotal()
            if (option == 1): calculateDailyTotal()
            elif (option == 2): calculateWeeklyTotal()
            elif (option == 3): calculateMonthlyTotal()
        case 4: 
            option = reportGenerator()
            if (option == 1): dailyReportMenu()
            elif(option == 2): weeklyReportMenu()
            elif(option == 3): monthlyReportMenu()
        case _: exit()