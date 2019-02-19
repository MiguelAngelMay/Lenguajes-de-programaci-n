"""
este programa ejemplifica el uso de funciones
El programa muestra el menu de una calculadora sencilla con las
operaciones basicas de suma, resta, multiplicacion y division
"""


# funcion que imprime el menu
# la funcion no recive ningun parametro
def menu():
    print("\n" * 50)  # varios cambios de lineas con el fin de limpiar la pantalla
    print("\t\t*** MENU ***\n")
    print("\t1. Suma")
    print("\t2. Resta")
    print("\t3. Multiplicacion")
    print("\t4. Division")
    print("\t5. Resultado")
    print("\t0. Salir")


# funcion opcion
# esta funcion muestra el menu, captura y valida la opcion del usuario
# recibe el numero menor, el mayor del menu y la opcion de salida (debe estar en el rango)
# devuelve una opcion valida del usuario
def opcion(min, max, salida):
    opcion = -1

    menu()  # dibuja el menu
    opcion = int(input("\n\t-> Opcion?: "))  # recibe una opcion del usuario
    while (opcion < min) or (opcion > max):
        print("\n\t>>> Error. Opcion invalida.")
        print("\t    Presione una tecla para continuar ...")
        input()  # detiene la ejecucion del programa hasta que se presione una tecla

        menu()  # dibuja el menu
        opcion = int(input("\n\t-> Opcion?: "))  # recibe una opcion del usuario

    return opcion


# funcion submenu
# esta funcion muestra el encabezado de un submenu
# no recive ningun parametro (argumento)
# no devuelve ningun valor
def submenu(titulo):
    print("\n" * 50)  # varios cambios de lineas con el fin de limpiar la pantalla
    # texto.upper() : combierte todo el texto en MAYUSCULAS
    print("\t\t*** " + titulo.upper() + " ***\n")


# funcion que calcula la suma de dos numero
def fSuma():
    submenu("SUMA")
    num1 = float(input("\tIngrese un numero: "))
    num2 = float(input("\tIngrese un numero: "))

    respuesta = num1 + num2

    # str(num) : es una funcion que convierte el numero num en texto
    print("\n\t-> El resultado de " + str(num1) + " + " + str(num2) + "= ", respuesta)
    print("\t   Presione cualquier tecla para continuar ...")
    input()
    return respuesta


# funcion que calcula la resta de dos numero
def fResta():
    submenu("RESTA")
    num1 = float(input("\tIngrese un numero: "))
    num2 = float(input("\tIngrese un numero: "))

    respuesta = num1 - num2

    # str(num) : es una funcion que convierte el numero num en texto
    print("\n\t-> El resultado de " + str(num1) + " - " + str(num2) + "= ", respuesta)
    print("\t   Presione cualquier tecla para continuar ...")
    input()
    return respuesta


# funcion que calcula la multiplicacion de dos numero
def fMultiplicacion():
    submenu("MULTIPLICACION")
    num1 = float(input("\tIngrese un numero: "))
    num2 = float(input("\tIngrese un numero: "))

    respuesta = num1 * num2

    # str(num) : es una funcion que convierte el numero num en texto
    print("\n\t-> El resultado de " + str(num1) + " * " + str(num2) + "= ", respuesta)
    print("\t   Presione cualquier tecla para continuar ...")
    input()
    return respuesta


# funcion que calcula la division de dos numero
def fDivision():
    submenu("division")  # no importa enviarlo en minuscula submenu la convierte
    num1 = float(input("\tIngrese un dividendo: "))
    num2 = float(input("\tIngrese un divisor: "))

    if num2 != 0:
        respuesta = num1 / num2

        # str(num) : es una funcion que convierte el numero num en texto
        print("\n\t-> El resultado de " + str(num1) + " / " + str(num2) + "= ", respuesta)
    else:
        # Division entre cero
        print("\n\t>>> Error. Division entre cero.")
        respuesta = "Error. Division entre cero."

    print("\t   Presione cualquier tecla para continuar ...")
    input()
    return respuesta


# funcion que muesta el ultimo resultado calculado
def fResultado(r):
    submenu("resultado")  # no importa enviarlo en minuscula submenu la convierte

    print("\n\t-> El ultimo resultado calculado fue: ", r)
    print("\t    Presione cualquier tecla para continuar ...")
    input()


def fSalida():
    submenu("Salida")  # no importa enviarlo en minuscula submenu la convierte

    print("\n\t-> Gracias por usarnos. Adios.  ")
    print("\t   Presione cualquier tecla para terminar ...")
    input()
    print("\n" * 50)  # varios cambios de lineas con el fin de limpiar la pantalla


# *************************
# *** PROGRAMA PRINCIAL ***
# *************************

resultado = 0
op = -1

while op != 0:
    op = opcion(0, 5, 0)  # llama a la funcion opcion

    if op == 1:
        ## funcion Suma
        resultado = fSuma()

    elif op == 2:
        ## funcion Resta
        resultado = fResta()

    elif op == 3:
        ## funcion Multiplicacion
        resultado = fMultiplicacion()

    elif op == 4:
        ## funcion Division
        resultado = fDivision()
    elif op == 5:
        ## funcion Resultado
        fResultado(resultado)
    else:
        ## funcion Salida
        resultado = fSalida()
