import os
from tabulate import tabulate
def Reports(equipos:list,sumTeams:int,divPromedio:int,promedio:float):
    os.system('cls')
    print('''
    ************** 
    *  REPORTES  *
    **************
    ''')
    for i, item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][5] < equipos[j][5]):
                aux = equipos[i]
                equipos[i] = equipos[j]
                equipos[j] = aux
    print(tabulate(equipos))
    topGoals = equipos[0][0]
    print(f'El equipo con mas goles fue {topGoals}')
    for i, item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][7] < equipos[j][7]):
                aux = equipos[i]
                equipos[i] = equipos[j]
                equipos[j] = aux
    print(tabulate(equipos))
    topPoints = equipos[0][0]
    print(f'El equipo con mas puntos fue {topPoints}')
    for i, item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][2] < equipos[j][2]):
                aux = equipos[i]
                equipos[i] = equipos[j]
                equipos[j] = aux
    print(tabulate(equipos))
    topWins = equipos[0][0]
    print(f'El equipo que mas partidos gano fue {topWins}')
    for item in equipos:
        sumTeams += item[5]
        divPromedio += 1
    promedio = sumTeams/divPromedio
    print(f'el total de puntos fue {sumTeams}')
    print(f'el promedio de goles entre los equipos fue {promedio}')
    os.system('pause')