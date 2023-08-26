#   2)
#Programa para mostrar un texto que el usuario digita 
# en letras grandes, hecho por Sergio Mostacero. 

#---------------------------------------------------------------------

# Importamos los módulos necesarios
from pyfiglet import Figlet
import random

# Solicitamos al usuario el nombre de una fuente a utilizar
font = input("Ingrese el nombre de una fuente a utilizar: ")

# Si el usuario no ingresa ninguna fuente, seleccionamos una al azar
if font == "":
    # Obtenemos la lista de fuentes disponibles
    fonts = Figlet().getFonts()
    # Seleccionamos una fuente al azar
    font = random.choice(fonts)

# Solicitamos al usuario un texto a imprimir
text = input("Ingrese un texto a imprimir: ")

# Creamos un objeto Figlet con la fuente seleccionada
figlet = Figlet(font=font)

# Generamos el texto con FIGlet
output = figlet.renderText(text)

# Mostramos el texto por pantalla
print(output)

#Fin del programa.
########################################################################
########################################################################
