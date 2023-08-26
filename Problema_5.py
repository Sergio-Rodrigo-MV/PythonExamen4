#   5)
#Programa para almacenar los datos de precio de bitcoin en un archivo
# txt y csv, hecho por Sergio Mostacero. 

#---------------------------------------------------------------------

# Importamos las librerías necesarias.
import requests
import json
import csv

# Definir la URL de la API que contiene los datos de precio de Bitcoin
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Hacer una petición GET a la URL y obtener la respuesta
response = requests.get(url)

# Comprobar que la respuesta tiene un código de estado 200 (éxito)
if response.status_code == 200:
    # Obtener el contenido de la respuesta como un diccionario de Python
    data = response.json()
    
    # Crear un archivo txt con el nombre "precio_bitcoin.txt" en modo escritura
    with open("precio_bitcoin.txt", "w") as txt_file:
        # Escribir el contenido del diccionario en el archivo txt
        json.dump(data, txt_file, indent=4)  # Indentación para que sea legible
        
    # Crear un archivo csv con el nombre "precio_bitcoin.csv" en modo escritura
    with open("precio_bitcoin.csv", "w", newline="") as csv_file:
        # Crear un objeto writer para escribir en el archivo csv
        writer = csv.writer(csv_file)
        
        # Escribir las filas del archivo csv
        for key, value in data["bpi"].items():
            writer.writerow([key, value["symbol"], value["rate"]])
else:
    # Si la respuesta no tiene un código de estado 200, mostrar un mensaje de error
    print(f"Ocurrió un error al obtener los datos de la web. Código de estado: {response.status_code}")
    
# Fin del programa.
########################################################################################################
########################################################################################################
