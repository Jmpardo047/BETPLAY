import os
from tabulate import tabulate
def ReportPoints(equipos:list):
    for i, item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][7] < equipos[j][7]):
                aux = equipos[i]
                equipos[i] = equipos[j]
                equipos[j] = aux
    print(tabulate(equipos))
    topPoints = equipos[0][0]
    print(f'El equipo con mas puntos fue {topPoints}')
    os.system('pause')
def ReportGoals(equipos:list):
    for i, item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][5] < equipos[j][5]):
                aux = equipos[i]
                equipos[i] = equipos[j]
                equipos[j] = aux
    print(tabulate(equipos))
    topGoals = equipos[0][0]
    print(f'El equipo con mas goles fue {topGoals}')
    os.system('pause')
def ReportWins(equipos:list):
    for i, item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][2] < equipos[j][2]):
                aux = equipos[i]
                equipos[i] = equipos[j]
                equipos[j] = aux
    print(tabulate(equipos))
    topWins = equipos[0][0]
    print(f'El equipo que mas partidos gano fue {topWins}')
    os.system('pause')
def ReportTotal(equipos:list,sumTeams:int,divPromedio:int,promedio:float):
    for item in equipos:
        sumTeams += item[5]
        divPromedio += 1
    promedio = sumTeams/divPromedio
    print(f'el total de puntos fue {sumTeams}')
    print(f'el promedio de goles entre los equipos fue {promedio}')
    os.system('pause')