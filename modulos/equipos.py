import os
def AddTeam(equipos:list):
    os.system('cls')
    nombre = str(input("Ingrese el nombre del equipo que quiere agregar\n )..")).upper()
    equipos.append([nombre,0,0,0,0,0,0,0])
    

def DltTeam(equipos:list):
    nombre = input('Ingrese el nombre del equipo a eliminar \n)..').upper()
    for i,item in enumerate(equipos):
        if (nombre in item):
            equipos.pop(i)
            break
        os.system('Pause')