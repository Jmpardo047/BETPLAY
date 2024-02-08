import os

def AddTeam(equipos:list):
    os.system('cls')
    nombre = str(input("Ingrese el nombre del equipo que quiere agregar\n )..")).upper()
    if (len(equipos)<=0):
        equipos.append([nombre,0,0,0,0,0,0,0])
    elif (validInfo(equipos,nombre) == False):
        equipos.append([nombre,0,0,0,0,0,0,0])
    else:
        AddTeam(equipos)    
def validInfo(equipos:list,nombre):
    for item in equipos:
        if (nombre in item):
            print('Este equipo ya ha sido agregado')
            os.system('pause')
            return True
    return False


def DltTeam(equipos:list):
    nombre = input('Ingrese el nombre del equipo a eliminar \n)..').upper()
    for i,item in enumerate(equipos):
        if (nombre in item):
            equipos.pop(i)
            break
        os.system('Pause')