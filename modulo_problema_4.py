# Función para crear un fichero con la tabla de multiplicar de un número
def crear_tabla(n):
    # Abrir el fichero en modo escritura
    with open(f"tabla-{n}.txt", "w") as f:
        # Recorrer los números del 1 al 10
        for i in range(1, 11):
            # Escribir la línea con el producto de n por i
            f.write(f"{n} x {i} = {n * i}\n")

# Función para leer un fichero con la tabla de multiplicar de un número y mostrarla por pantalla
def leer_tabla(n):
    try:
        # Abrir el fichero en modo lectura
        with open(f"tabla-{n}.txt", "r") as f:
            # Leer todo el contenido del fichero
            contenido = f.read()
            # Mostrar el contenido por pantalla
            print(contenido)
    except FileNotFoundError:
        # Si el fichero no existe, mostrar un mensaje de error
        print(f"No se encontró el fichero tabla-{n}.txt")

# Función para leer una línea específica de un fichero con la tabla de multiplicar de un número y mostrarla por pantalla
def leer_linea(n, m):
    try:
        # Abrir el fichero en modo lectura
        with open(f"tabla-{n}.txt", "r") as f:
            # Leer todas las líneas del fichero como una lista
            lineas = f.readlines()
            # Obtener la línea m-ésima (se resta 1 porque las listas empiezan en 0)
            linea = lineas[m - 1]
            # Mostrar la línea por pantalla
            print(linea)
    except FileNotFoundError:
        # Si el fichero no existe, mostrar un mensaje de error
        print(f"No se encontró el fichero tabla-{n}.txt")
    except IndexError:
        # Si la línea m no existe, mostrar un mensaje de error
        print(f"No existe la línea {m} en el fichero tabla-{n}.txt")

# Función para validar que un número está entre 1 y 10
def validar_numero(num):
    # Convertir el número a entero si es posible
    try:
        num = int(num)
    except ValueError:
        # Si no es posible, devolver False
        return False
    # Comprobar que el número está entre 1 y 10
    if num >= 1 and num <= 10:
        # Si es así, devolver True
        return True
    else:
        # Si no, devolver False
        return False
