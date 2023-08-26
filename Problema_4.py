#   4)
#Programa para mostrar la tabla de multiplicar según el número
#que ingrese el usuario, hecho por Sergio Mostacero. 

#---------------------------------------------------------------------


import modulo_problema_4

# Función para mostrar el menú de opciones y solicitar una opción al usuario
def mostrar_menu():
    # Mostrar las opciones disponibles
    print("Elige una opción:")
    print("1. Crear un fichero con la tabla de multiplicar de un número")
    print("2. Leer un fichero con la tabla de multiplicar de un número y mostrarla por pantalla")
    print("3. Leer una línea específica de un fichero con la tabla de multiplicar de un número y mostrarla por pantalla")
    print("4. Salir del programa")
    # Solicitar una opción al usuario y devolverla como entero
    opcion = int(input("Introduce tu opción: "))
    return opcion

# Programa principal
# Repetir hasta que se elija la opción 4 (salir)
def main():
   while True:
    # Mostrar el menú y obtener la opción elegida
    opcion = mostrar_menu()
    # Si la opción es 1 (crear fichero)
    if opcion == 1:
        # Solicitar un número entre 1 y 10 al usuario y validar que sea correcto
        numero = input("Introduce un número entre 1 y 10: ")
        while not modulo_problema_4.validar_numero(numero):
            print("Número inválido. Inténtalo de nuevo.")
            numero = input("Introduce un número entre 1 y 10: ")
        # Convertir el número a entero
        numero = int(numero)
        # Crear el fichero con la tabla de multiplicar del número
        modulo_problema_4.crear_tabla(numero)
        print(f"Se ha creado el fichero tabla-{numero}.txt")
    # Si la opción es 2 (leer fichero)
    elif opcion == 2:
        # Solicitar un número entre 1 y 10 al usuario y validar que sea correcto
        numero = input("Introduce un número entre 1 y 10: ")
        while not modulo_problema_4.validar_numero(numero):
            print("Número inválido. Inténtalo de nuevo.")
            numero = input("Introduce un número entre 1 y 10: ")
        # Convertir el número a entero
        numero = int(numero)
        # Leer el fichero con la tabla de multiplicar del número y mostrarla por pantalla
        modulo_problema_4.leer_tabla(numero)
    # Si la opción es 3 (leer línea)
    elif opcion == 3:
        # Solicitar dos números entre 1 y 10 al usuario y validar que sean correctos
        numero = input("Introduce un número entre 1 y 10: ")
        while not modulo_problema_4.validar_numero(numero):
            print("Número inválido. Inténtalo de nuevo.")
            numero = input("Introduce un número entre 1 y 10: ")
        linea = input("Introduce una línea entre 1 y 10: ")
        while not modulo_problema_4.validar_numero(linea):
            print("Línea inválida. Inténtalo de nuevo.")
            linea = input("Introduce una línea entre 1 y 10: ")
        # Convertir los números a enteros
        numero = int(numero)
        linea = int(linea)
        # Leer la línea específica del fichero con la tabla de multiplicar del número y mostrarla por pantalla
        modulo_problema_4.leer_linea(numero, linea)
    # Si la opción es 4 (salir)
    elif opcion == 4:
        # Terminar el programa
        print("Gracias por usar el programa. Hasta pronto.")
        break
    # Si la opción no es válida
    else:
        # Mostrar un mensaje de error
        print("Opción inválida. Inténtalo de nuevo.")
        
if __name__== '__main__':
     main()
     
# Fin del programa.
#############################################################################################################
#############################################################################################################