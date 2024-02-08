import modulos.menu as m
import modulos.equipos as teams
import modulos.registro as reg
import modulos.reportes as reps
import modulos.menureps as menureps
from tabulate import tabulate
equipos = []
regFechas = []
sumTeams = 0
divPromedio = 0
promedio = 0.0
isDuplicate = True
isActive = True
while isActive:
    m.os.system('cls')
    n = m.MenuPrincipal()
    if (n == 1):
        teams.AddTeam(equipos)
    elif (n == 2):
        teams.DltTeam(equipos)
    elif ( n == 3):
        menureps.MenuReportes(equipos,sumTeams,divPromedio,promedio)
    elif (n == 4):
        isExist = False
        m.os.system('cls')
        fechaJuego = str(input("Ingrese la fecha del juego\n ).."))
        while isExist == False:
            m.os.system('cls')
            tm1 = str(input("Ingrese el equipo Local\n )..")).upper()
            for item in equipos:
                if (tm1 in item ):
                    gTm1 = int(input("Goles anotados por el equipo Local\n ).."))
                    isExist=True
        isExist=False
        while isExist == False:
            m.os.system('cls')
            tm2 = str(input("Ingrese el equipo Visitante\n )..")).upper()
            for item in equipos:
                if (tm2 in item ):
                    gTm2 = int(input("Goles anotados por el equipo Visitante\n ).."))
                    isExist=True
        reg.RegTm(gTm1,gTm2,fechaJuego,tm1,tm2,regFechas,equipos)
    elif (n == 5):
            print(tabulate(equipos, headers = ["nombre","PJ","PG","PP","PE","GF","GC","TP"]))
            m.os.system('pause')
    elif (n == 6):
        m.os.system('cls')
        print(tabulate(regFechas, headers = ["Fecha","Local","Visitante","Goles Local","Goles Visitantes","Ganador","Perdedor"]))
        m.os.system('Pause')
    elif (n == 7):
        isActive = False
        m.os.system('cls')
        print("Hasta pronto")
        m.os.system("pause")
    else:
        m.os.system('cls')
        print("La opcion ingresada no es valida")
        m.os.system('pause')       
