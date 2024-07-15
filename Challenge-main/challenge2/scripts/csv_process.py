from datetime import datetime
from csv_operations import *
import pandas as pd

def main():
    """
    Función principal que ejecuta todas las transformaciones y guarda el resultado en un CSV.
    """
    # URL pública del archivo de Google Sheets exportado como CSV
    input_file = 'https://docs.google.com/spreadsheets/d/1TvyXkNu2cVQYOJ0x-Gg4rjHq8jb_6JryEX1NgFbDmjA/export?format=csv&gid=1544984482'
    df = read_csv(input_file)

    # Ordenar el archivo original solo por 'OLT_NAME' y 'TIMESTAMP'
    df_original_sorted = order_by_columns(df.copy(), ['OLT_NAME', 'TIMESTAMP'])

    #Asegurate de modificar la ruta para que se guarde en la ruta que desees.
    #Por Ejemplo: Ruta/a/tu/carpeta/Challenge-mainn/Challenge-main/challenge2/data/original/gpon_challenge_sorted.csv
    save_to_csv(df_original_sorted, 'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge2/data/original/gpon_challenge_sorted.csv')
    
    # Transformaciones
    df = add_dn_column(df)

    # Resamplear y sumar KPIs
    df_resampled = resample_and_sum_kpis(df)

    # Ordenar por columnas
    df_resampled = order_by_columns(df_resampled, ['DN', 'TIMESTAMP'])

    # Guardar el archivo resampleado y ordenado
    output_filename = datetime.now().strftime('GPON_CSV_OUTPUT-%H-%M-%S.csv')
    
    #Asegurate de modificar la ruta para que se guarde en la ruta que desees.
    #Por Ejemplo: Ruta/a/tu/carpeta/Challenge-mainn/Challenge-main/challenge2/data/transformed/
    save_to_csv(df_resampled, f'C:/Users/Usuario/Documents/Challenge-mainn/Challenge-main/challenge2/data/transformed/{output_filename}')

if __name__ == '__main__':
    main()