import os 
opciones ="1. Agregar equipo\n2. eliminar equipo\n3. reportes\n4. Agregar fecha jugada\n5. Ver tabla de equipos\n6. Ver registro de fechas\n7. salir "
titulo = '''
    *****************************
    *  BIENVENIDO A LA BETPLAY  *
    *****************************
'''
def MenuPrincipal()->int:
    lstOpciones = [1,2,3,4,5,6,7]
    os.system('cls')
    print(titulo)
    try:
        print(opciones)
        n = int(input(").."))
        if (n not in lstOpciones):
            MenuPrincipal()
    except ValueError:
        print('dato invalido')
        os.system('pause')
        MenuPrincipal()
    else:
        return n