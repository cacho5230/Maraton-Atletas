# IMPORTACIONES
from claseAtleta import Atletas, Inscripciones
import random

### EXTRAS ###

# LISTA MENU
opcionesMenu = ['1- Inscribir',
                '2- Registrar posiciones',
                '3- Mostrar Tabla de Posiciones',
                '4- Mostrar todos los Atletas',
                '5- Borrar atleta por codigo',
                '6- Crear atleta nuevo',
                '7- Salir']


### FUNCIONES ###

# FUNCION VALIDADORA DE ENTRADA

def insertInput(tipo, texto):

    # VALIDA STRINGS
    if tipo == "String":
        while True:
            UserInput = input(texto)
            try:
                if UserInput.isnumeric():
                    print("No ingrese numeros, solo texto !")
                elif UserInput == "":
                    print("No ingrese valores vacios !")
                else:
                    return UserInput
            except ValueError:
                print("Datos incorrectos")

    # VALIDA NUMEROS ENTEROS
    elif tipo == "Numero":
        while True:
            UserInput = input(texto)
            try:
                if UserInput.isnumeric():
                    UserInput = int(UserInput)
                    return UserInput
                elif UserInput == "":
                    print("No ingrese valores vacios !")
                else:
                    print("Entrada Incorrecta: Escribe un numero entero")
            except ValueError:
                print("Datos incorrectos")

    # VALIDA OPCIONES DEL MENU
    elif tipo == "Opcion":
        while True:
            UserInput = input(texto)
            try:
                if UserInput.isnumeric():
                    UserInput = int(UserInput)
                    if UserInput >= 1 and UserInput <= 7:
                        return UserInput
                    else:
                        print("Opcion incorrecta !")
                elif UserInput == "":
                    print("No ingrese valores vacios !")
                else:
                    print("Entrada Incorrecta: Escribe un numero entero")
            except:
                print('Datos incorrectos')

# FUNCION MENU

def menuPrincipal(opcionesMenu):
    nombre = insertInput(
        "String", "Por favor ingrese su nombre antes de continuar: \n")
    print(f'\nBienvenido/a {nombre.upper()}\n')
    while True:
        for i in opcionesMenu:
            print(i)
        opcion = insertInput("Opcion", "Ingrese una opción:\n")
        if opcion == 7:
            print("Gracias por usar este sistema " +
                  nombre.upper()+"\nHasta Luego :)")
            break
        ejecutarOpcion(opcion)

# FUNCION MAIN


def ejecutarOpcion(opcion):

    if opcion == 1:
        print('-= Inscripcion de Atletas =-\n')
        # Recorrido de tabla atleta, solicitar distancia para cada uno y asignar un dorsal aleatorio
        atletas = Atletas.conseguir_todos_atletas()
        if atletas:
            for i in atletas:
                atletaDato = (
                    f"Código: {int(i[0])}. | Apellido: {i[1]}  Nombre: {i[2]}  Edad: {i[3]}")
                print(atletaDato)

                inscripcion = {
                    'idatleta': 0,
                    'distancia': 0,
                    'dorsal': 0,
                    'tiempo': '',
                    'posicion': 0
                }

                print("km disponibles - 5KM - 10KM - 42KM")
                distancia = insertInput(
                    "Numero", "Por favor, ingrese una distancia:\n")
                if distancia == 5 or distancia == 10 or distancia == 42:
                    dorsal = random.randint(0, 99)
                    print("DORSAL ASIGNADO ALEATORIAMENTE: "+str(dorsal))
                    inscripcion['idatleta'] = i[0]
                    inscripcion['distancia'] = distancia
                    inscripcion['dorsal'] = dorsal
                    Inscripciones.inscribir_atleta(inscripcion)
                    print("\n¡¡ DATOS CARGADOS CORRECTAMENTE !!\n")

                else:
                    print("ingresa un valor correcto (5 - 10 - 42)")

        else:
            print('No hay atletas disponibles\n')

    elif opcion == 2:
        print('-= Registrar posiciones de atletas =-\n')
        atletas = Inscripciones.conseguir_posiciones_atletas()
        if atletas:
            for i in atletas:

                atletaDato = (
                    f"Código: {int(i[0])}. | Apellido: {i[1]}  Nombre: {i[2]}  Edad: {i[3]} Dorsal: {i[6]}°  Distancia: {i[7]}km")
                print(atletaDato)

                inscripcion = {
                    'idatleta': 0,
                    'distancia': 0,
                    'dorsal': 0,
                    'tiempo': '',
                    'posicion': 0
                }

                print("\nFORMATO DE TIEMPO: -HS--M--S")
                tiempo = insertInput(
                    "String", "Por favor, introduce el tiempo del atleta: \n")
                posicion = insertInput(
                    "Numero", "ingresa la posicion del atleta: \n")
                inscripcion['idatleta'] = i[0]
                inscripcion['tiempo'] = tiempo
                inscripcion['posicion'] = posicion
                Inscripciones.registrar_posicion_atleta(inscripcion)
            print("\n¡¡ DATOS CARGADOS CORRECTAMENTE !!\n")
        else:
            print("No hay atletas disponibles o falta registrar distancia\n")

    elif opcion == 3:
        print('-= Mostrando posiciones de todos los atletas =-\n')
        atletas = Inscripciones.mostrar_posiciones()
        if atletas:
            print("{:^12}{:^12}{:^8}{:^12}{:^12}".format(
                "POSICION", "TIEMPO", "DORSAL", "APELLIDO", "NOMBRE"))
            print("{}".format("+"*55))
            try:
                for i in atletas:
                    print("{:^12}{:^12}{:^8}{:^12}{:^12}".format(
                        i[0], i[1], i[2], i[3], i[4]))
                print(" ")
            except:
                print("\nError, faltan datos, no se puede mostrar correctamente\n")
        else:
            print("No se encontraron registros\n")

    elif opcion == 4:
        print('-= Mostrando todos los datos de los atletas =-\n')
        atletas = Atletas.conseguir_todos_atletas()
        if atletas:
            for i in atletas:
                datos = "Código: {0}. | Apellido: {1}  Nombre: {2}  Edad: {3}"
                print(datos.format(i[0], i[1], i[2], i[3]))
            print("\n")
        else:
            print("No hay atletas disponibles\n")

    elif opcion == 5:
        print('-= Borrar atleta cargado =-\n')
        atletas = Atletas.conseguir_todos_atletas()
        if atletas:
            for i in atletas:
                datos = "Código: {0}. | Apellido: {1}  Nombre: {2}  Edad: {3}"
                print(datos.format(i[0], i[1], i[2], i[3]))
            
            id = insertInput(
                "Numero", "\nIngrese el codigo del Atleta a eliminar: ")
            for i in atletas:
                if i[0] == id:
                    Atletas.eliminar_atleta(id)
                    print("\nATLETA ELIMINADO CORRECTAMENTE !\n")
                    break
                else:
                    print("\nNo existe atleta con ese codigo\n")
        else:
            print("No hay atletas disponibles para eliminar\n")
    
    elif opcion == 6:
        print('-= Crear atleta nuevo =-\n')
        
        atletaDic = {
                    'idatleta': 0,
                    'apellido': '',
                    'nombre': '',
                    'edad': 0
                }

        apellido = insertInput(
            "String", "Por favor, introduce el apellido del atleta: \n")
        nombres = insertInput(
            "String", "ingresa el/los nombres del atleta: \n")
        edad = insertInput(
            "Numero", "ingresa la edad del atleta: \n")
        atletaDic['apellido'] = apellido
        atletaDic['nombre'] = nombres
        atletaDic['edad'] = edad
        Atletas.crear_atleta_nuevo(atletaDic)
        print("\nATLETA CARGADO CORRECTAMENTE\n")
    
    
    else:
        print('Opción Incorrecta: Ingrese una opcion válida\n')

    

# CORRER LA APP
menuPrincipal(opcionesMenu)
