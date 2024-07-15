import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import sys
sys.path.append('C:\\Users\\Usuario\\Documents\\Challenge-mainn\\Challenge-main\\challenge2\\scripts')

# Importar las funciones del archivo csv_operations.py
from csv_operations import * 

def main():
    """
    Función principal que ejecuta todas las transformaciones y guarda el resultado en un CSV.
    """
    # URL pública del archivo de Google Sheets exportado como CSV
    input_file = 'https://docs.google.com/spreadsheets/d/1TvyXkNu2cVQYOJ0x-Gg4rjHq8jb_6JryEX1NgFbDmjA/export?format=csv&gid=1544984482'
    mongo_uri = 'mongodb://root:root@localhost:8007/'
    db_name = 'gpon'
    collection_name = 'gpon_olt'
    
    # Cargar el CSV en MongoDB
    load_csv_to_mongo(input_file, db_name, collection_name, mongo_uri)
    
    # Exportar la colección a un archivo JSON
    export_collection_to_json(db_name, collection_name, mongo_uri, 'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge1/data/original/gpon_olt.json')

    # Transformar json a CSV para poder transformar el dataset con las funciones ya definidas
    json_file_path = 'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge1/data/original/gpon_olt.json'
    csv_file_path = 'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge1/data/original/gpon_olt.csv'
    
    # Convertir JSON a CSV
    json_to_csv(json_file_path, csv_file_path)
    
    # Realizar las transformaciones
    df = read_csv(csv_file_path)

    # Ordenar el archivo original solo por 'OLT_NAME' y 'TIMESTAMP'
    df_original_sorted = order_by_columns(df.copy(), ['OLT_NAME', 'TIMESTAMP'])

    # Asegurate de modificar la ruta para que se guarde en la ruta que desees.
    save_to_csv(df_original_sorted, 'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge1/data/original/gpon_challenge_sorted.csv')
    
    # Transformaciones
    df = add_dn_column(df)

    # Resamplear y sumar KPIs
    df_resampled = resample_and_sum_kpis(df)

    # Ordenar por columnas
    df_resampled = order_by_columns(df_resampled, ['DN', 'TIMESTAMP'])

    # Guardar el archivo resampleado y ordenado
    output_filename = datetime.now().strftime('GPON_CSV_OUTPUT-%H-%M-%S.csv')
    
    # Asegurate de modificar la ruta para que se guarde en la ruta que desees.
    save_to_csv(df_resampled, f'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge1/data/transformed/{output_filename}')

if __name__ == '__main__':
    main()