
# Challenge 1

## Descripción del Proyecto

Este proyecto automatiza el procesamiento y transformación de datos de KPIs de dispositivos OLT en una red GPON utilizando una base de datos MongoDB Dockerizada. Los datos de KPIs se cargan en una colección MongoDB desde un archivo CSV, se exportan a un archivo JSON, y luego se transforman mediante un script Python. Las transformaciones incluyen convertir nombres de OLT a mayúsculas, agregar una columna DN con el formato "OLT/(nombre OLT)", y resamplear los KPIs (ESTABLISHED_CALLS, FAILED_CALLS, NEW_REG, EXPIRED_REG, FAILED_REG, GONE_REG, UNAUTHORIZED_REG) por OLT cada 15 minutos. Los datos transformados se guardan en un archivo CSV. Además, se proporciona una línea de crontab para ejecutar el script de transformación automáticamente cada 15 minutos en un servidor Linux. El repositorio de GitHub incluye los archivos CSV, scripts, Dockerfile de MongoDB y una página Markdown.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:
 - `Challenge-main/` 
  - `challenge1/`
    - `data/`: Contiene los datos originales y transformados.
      - `original/`: Archivos CSV y JSON originales.
      - `transformed/`: Archivos CSV transformados.
    - `scripts/`: Contiene los scripts Python para la carga y transformación de datos.
      - `procesamiento_csv.py/`: Contiene el archivo main que ejecuta el proyecto.
    - `mongodb/`: Carpeta que contiene el dockerfile
      - `data/`: Contiene los datos de la BD Mongo.
      - `docker-compose.yml`: Archivo de configuración de Docker Compose para levantar el contenedor de MongoDB.
      - `init.js`: Archivo que contiene la definición de la creación de la BD y la colección "gpon_olt".
    - `README.md`: Este archivo de documentación.
  - `challenge2/`
    - `data/`: Contiene los datos originales y transformados.
      - `original/`: Archivos CSV originales.
      - `transformed/`: Archivos CSV transformados.
    - `scripts/`: Contiene los scripts Python para la transformación de datos.
      - `csv_operations.py`: Módulo con las operaciones necesarias para ejecutar el script principal.
      - `csv_process.py`: Contiene el archivo main que ejecuta el proyecto.
    - `READ.md`

 
## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos instalados:

- Docker
- Docker Compose
- Python 3.7 o superior
- Librerías Python: `pandas`, `pymongo`

## Windows
1. Open Command Prompt or PowerShell as Administrator.
2. Asegurate de que el sistema de gestión de paquete de Python (pip) esté actualizado:
   ```sh
   python -m pip install --upgrade pip
   ```
3. Install pandas:
   ```sh
   pip install pandas
   ```
4. Install pymongo:
   ```sh
   pip install pymongo
   ```
## Linux
1. Open your terminal.
2. Update your package list:
   ```sh
   sudo apt update
   ```
3. Install pip, the Python package installer, if you don't have it already:
   ```sh
   sudo apt install python3-pip
   ```
4. Install pandas:
   ```sh
   pip3 install pandas
   ```
5. Install pymongo:
   ```sh
   pip3 install pymongo
   ```
## Configuración del Servidor MongoDB y ejecución del script

Para configurar y levantar el servidor MongoDB, sigue estos pasos:

1. Ejecutar docker.

2. Desde la terminal ir hasta la ruta donde se encuentra alojado el contenedor docker:

    ```bash
    cd /ruta/absoluta/hasta/mongodb
    ```

3. Levanta el contenedor de MongoDB usando Docker Compose:
    ```bash
    docker-compose up 
    ```
 Esto levantará un servidor MongoDB accesible en `localhost:8007` con las credenciales `root:root`.

 3. Ejecutar el script:
    
    windows
    ```bash
     python ruta/absoluta/a/procesamiento_csv.py
    ```
    linux
    ```bash
     python3 ruta/absoluta/a/procesamiento_csv.py
    ```

   
    











