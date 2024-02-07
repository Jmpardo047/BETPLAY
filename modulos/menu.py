import os 
opciones ="1. Agregar equipo\n2. eliminar equipo\n3. reportes\n4. Agregar fecha jugada\n5. Ver tabla de equipos\n6. Ver registro de fechas\n7. salir "
titulo = '''
    *****************************
    *  BIENVENIDO A LA BETPLAY  *
    *****************************
'''
def MenuPrincipal()->int:
    os.system('cls')
    print(titulo)
    print(opciones)
    n = int(input(").."))
    return n