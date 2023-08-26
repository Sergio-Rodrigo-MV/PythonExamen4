#   3)
#Programa para descargar una imagen de la web.

#---------------------------------------------------------------------

# Importamos la librería request
import requests

# Proporcionamos la url necesaria.
url = 'https://images.unsplash.com/photo-1591160690555-5debfba289f0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=464&q=80'

response = requests.get(url)

with open('perro_imagen.jpg', 'wb') as f:
    f.write(response.content)
    pass

# Fin del programa.
###############################################################################
###############################################################################
