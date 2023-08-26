#   6)
#Programa para generar una base de datos llamada 'cryptos' donde 
# se generará una base de datos llamada bitcoin el cúal debera el precio del 
# bitcoin, hecho por Sergio Mostacero. 

#---------------------------------------------------------------------

# Importamos las librerías necesarias.
import requests
import json
import sqlite3
from datetime import datetime

try:
    # Solicitamos al usuario la cantidad de bitcoins que posee
    n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    
    # Consultamos en la API de CoinDesk para obtener el precio actual de Bitcoin
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    
    # Obtenemos las fechas y precios en las monedas necesarias
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    precio_usd = data["bpi"]["USD"]["rate_float"]
    precio_gbp = data["bpi"]["GBP"]["rate_float"]
    precio_eur = data["bpi"]["EUR"]["rate_float"]
    
    # Calculamos los costos actuales de "n" Bitcoins en diferentes monedas
    costo_usd = n * precio_usd
    costo_gbp = n * precio_gbp
    costo_eur = n * precio_eur
    
    # Mostramos los costos actuales de "n" Bitcoins en diferentes monedas
    print(f"El costo actual de {n:.4f} Bitcoins en USD es: ${costo_usd:,.4f}")
    print(f"El costo actual de {n:.4f} Bitcoins en GBP es: £{costo_gbp:,.4f}")
    print(f"El costo actual de {n:.4f} Bitcoins en EUR es: €{costo_eur:,.4f}")
    
    # Creamos o conectamos a la base de datos "cryptos"
    conn = sqlite3.connect("cryptos.db")
    cursor = conn.cursor()
    
    # Creamos la tabla "bitcoin" si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY,
            fecha TEXT,
            cantidad_bitcoins REAL,
            costo_usd REAL,
            costo_gbp REAL,
            costo_eur REAL
        )
    ''')
    
    # Insertamos los datos en la tabla
    cursor.execute('''
        INSERT INTO bitcoin (fecha, cantidad_bitcoins, costo_usd, costo_gbp, costo_eur)
        VALUES (?, ?, ?, ?, ?)
    ''', (fecha_actual, n, costo_usd, costo_gbp, costo_eur))
    
    # Finalmente guardamos los cambios y cerramos la conexión
    conn.commit()
    conn.close()
    
    print("Datos de Bitcoin almacenados en la base de datos.")
    
except ValueError:
    print("Error: Por favor, ingrese una cantidad válida de Bitcoins.")
except requests.RequestException:
    print("Error: No se pudo conectar a la API de CoinDesk.")
    
# Fin del programa.
############################################################################################
############################################################################################
