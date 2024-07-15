
# Challenge 2

## Descripción del Proyecto

Este proyecto automatiza el procesamiento y transformación de datos de KPIs de dispositivos OLT en una red GPON. Los datos se leen de un archivo CSV, se aplican varias transformaciones, y se guardan en un nuevo archivo CSV. Además, se proporciona una línea de crontab para ejecutar el script de transformación automáticamente cada 15 minutos en un servidor Linux. El repositorio de GitHub incluye los archivos CSV, scripts y una página Markdown con la línea de crontab.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:
 - `Challenge-main/` 
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

- Python 3.7 o superior
- Librerías Python: `pandas`

### Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta los siguientes comandos:

#### Windows

1. Abre el Símbolo del sistema o PowerShell como Administrador.
2. Asegúrate de que el sistema de gestión de paquete de Python (pip) esté actualizado:
   ```sh
   python -m pip install --upgrade pip
   ```
3. Instala pandas:
   ```sh
   pip install pandas
   ```

#### Linux

1. Abre tu terminal.
2. Actualiza tu lista de paquetes:
   ```sh
   sudo apt update
   ```
3. Instala pip, el instalador de paquetes de Python, si no lo tienes ya:
   ```sh
   sudo apt install python3-pip
   ```
4. Instala pandas:
   ```sh
   pip3 install pandas
   ```

## Ejecución del script

 - Ejecutar el script:
    
    windows
    ```bash
     python ruta/absoluta/a/csv_process.py
    ```
    linux
    ```bash
     python3 ruta/absoluta/a/csv_process.py
    ```


