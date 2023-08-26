# Cuarta Práctica de Python.

#  1)
#Programa para solicitar al usuario cuantos bitcoins posee y su 
#valor en dolares, hecho por Sergio Mostacero.

#------------------------------------------------------------------------------

# Importamos las librerías necesarias
import requests
import json

# Solicitamos al usuario la cantidad de bitcoins que posee
n = float(input("Ingrese la cantidad de bitcoins que posee: "))
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
# Consultamos la API de CoinDesk
try:
    # Hacemos la petición HTTP a la URL de la API
    response = requests.get(url)
    # Verificamos si la petición fue exitosa
    if response.status_code == 200:
       
        content = response.text
        # Convertimos la cadena a un objeto JSON
        data = json.loads(content)
        # Obtenemos el precio actual de Bitcoin en USD del objeto JSON
        price = data["bpi"]["USD"]["rate_float"]
        # Calculamos el costo actual de n bitcoins en USD
        cost = price * n
        # Damos formato al resultado con cuatro decimales y separador de miles
        amount = format(cost, ",.4f")
        # Mostramos el resultado por pantalla usando una cadena formateada
        print(f"El costo actual de {n} bitcoins en USD es ${amount}")
    else:
        # Mostramos un mensaje de error si la petición no fue exitosa
        print(f"Ocurrió un error al consultar la API: {response.status_code}")
except requests.RequestException as error:
    # Mostramos un mensaje de error si ocurrió una excepción al hacer la petición
    print(f"Ocurrió una excepción al consultar la API: {error}")
    
# Fin del programa.
####################################################################################+
####################################################################################
