#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys

# Verificar si se proporcionó un argumento para el archivo HTML
if len(sys.argv) != 2:
    print("Uso: python3 extract.py <ruta_al_archivo_html>")
    sys.exit(1)

archivo = sys.argv[1]

# Leer el archivo HTML
with open(archivo, "r") as archivo_html:
    contenido = archivo_html.read()

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(contenido, "html.parser")

# Buscar todas las etiquetas tr con la clase config-var-item
rows = soup.find_all("tr", class_="config-var-item")

# Iterar sobre las filas y extraer los datos
for row in rows:
    key = row.find("input")["value"]
    value = row.find("textarea").text.strip()
    print(f"{key}={value}")
