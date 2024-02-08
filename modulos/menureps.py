import os
import modulos.reportes as reps
def MenuReportes(equipos:list,sumTeams:int,divPromedio:int,promedio:float):
    lstOpciones = [1,2,3,4,5]
    os.system('cls')
    print('''
        ************** 
        *  REPORTES  *
        **************
    ''')
    try:
        print('1. Tabla de puntos\n2. Tabla de goles anotados\n3. Tabla de partidos ganados\n4. total de goles y promedio\n5. salir')
        op = int(input(')..'))
        if (op not in lstOpciones):
            MenuReportes(equipos,sumTeams,divPromedio,promedio)
    except ValueError:
        print('dato invalido')
        os.system('pause')
        MenuReportes(equipos,sumTeams,divPromedio,promedio)
    else:
        if (op == 1):
            reps.ReportPoints(equipos)
        elif (op == 2):
            reps.ReportGoals(equipos)
        elif (op == 3):
            reps.ReportWins(equipos)
        elif (op == 4):
            reps.ReportTotal(equipos,sumTeams,divPromedio,promedio)
        elif (op == 5):
            pass
