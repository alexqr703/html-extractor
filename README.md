# Extractor de Datos Clave=Valor de Archivos .HTML con Python

Este script de Python te permite extraer datos en formato clave=valor de archivos HTML de manera sencilla. Utiliza la biblioteca BeautifulSoup para analizar y extraer información de los archivos HTML especificados.

## Requisitos previos

Asegúrate de tener Python 3 instalado en tu sistema. Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/).

Para configurar el entorno virtual y instalar las dependencias necesarias, sigue estos pasos:

```bash
sudo apt update
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install beautifulsoup4
```

## Uso

Una vez configurado el entorno y las dependencias instaladas, puedes ejecutar el script `extract.py` proporcionando la ruta al archivo HTML del que deseas extraer los datos. Puedes hacerlo de la siguiente manera:

```bash
python3 extract.py "archivo.html"
```
o
```bash
python3 extract.py /ruta/completa/a/"archivo.html"
```
