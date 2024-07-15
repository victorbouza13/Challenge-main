
import pandas as pd
from pymongo import MongoClient
import json

def read_csv(file_path):
    """
    Lee el archivo CSV y devuelve un DataFrame.

    Args:
        file_path (str): La ruta del archivo CSV.

    Returns:
        DataFrame: El DataFrame con los datos del CSV.
    """
    return pd.read_csv(file_path)

def add_dn_column(df):
    """
    Convierte todos los nombres de OLT a mayúsculas y les agrega el prefijo "OLT/" en una nueva columna 'DN'.

    Args:
        df (DataFrame): El DataFrame con los datos originales.

    Returns:
        DataFrame: El DataFrame con la columna 'OLT_NAME' convertida a mayúsculas y la nueva columna 'DN' añadida.
    """
    df['OLT_NAME'] = df['OLT_NAME'].str.upper()
    df['DN'] = 'OLT/' + df['OLT_NAME']
    return df


def resample_and_sum_kpis(df):
    """
    Resamplea la información cada 15 minutos y suma los KPIs especificados.

    Args:
        df (DataFrame): El DataFrame con los datos originales.

    Returns:
        DataFrame: El DataFrame con los datos resampleados y los KPIs sumados.
    """
    kpis_to_sum = ['ESTABLISHED_CALLS', 'FAILED_CALLS', 'NEW_REG', 'EXPIRED_REG', 'FAILED_REG', 'GONE_REG', 'UNAUTHORIZED_REG']
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    df.set_index('TIMESTAMP', inplace=True)
    df_resampled = df.groupby(['OLT_NAME', 'DN']).resample('15min')[kpis_to_sum].sum()
    df_resampled.reset_index(inplace=True)
    return df_resampled

def save_to_csv(df, file_path):
    """
    Guarda el DataFrame transformado en un archivo CSV.

    Args:
        df (DataFrame): El DataFrame con los datos transformados.
        file_path (str): La ruta donde se guardará el archivo CSV.
    """
    df.to_csv(file_path, index=False)

def order_by_columns(df, columns):
    """
    Ordena el DataFrame por las columnas especificadas en orden ascendente.

    Args:
        df (pandas.DataFrame): El DataFrame a ordenar.
        columns (list): Lista de nombres de columnas por las cuales se ordenará el DataFrame.

    Returns:
        pandas.DataFrame: El DataFrame ordenado.
    """
    df.sort_values(by=columns, inplace=True)
    return df

def load_csv_to_mongo(csv_url, db_name, collection_name, mongo_uri):
    """
    Carga un CSV desde una URL en una colección de MongoDB, eliminando primero todos los documentos existentes.

    Args:
        csv_url (str): La URL del archivo CSV.
        db_name (str): El nombre de la base de datos.
        collection_name (str): El nombre de la colección.
        mongo_uri (str): El URI de conexión a MongoDB.
    """
    # Leer el CSV desde la URL
    df = pd.read_csv(csv_url)
    
    # Conectar a MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Eliminar todos los documentos existentes en la colección
    collection.delete_many({})
    print(f"Todos los documentos de la colección '{collection_name}' en la base de datos '{db_name}' han sido eliminados.")
    
    # Cargar el DataFrame en MongoDB
    collection.insert_many(df.to_dict('records'))
    print(f"Datos cargados en la colección '{collection_name}' de la base de datos '{db_name}'.")

def export_collection_to_json(db_name, collection_name, mongo_uri, output_file):
    """
    Exporta una colección de MongoDB a un archivo JSON.

    Args:
        db_name (str): El nombre de la base de datos.
        collection_name (str): El nombre de la colección.
        mongo_uri (str): El URI de conexión a MongoDB.
        output_file (str): La ruta del archivo JSON de salida.
    """
    # Conectar a MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Obtener todos los documentos de la colección
    documents = collection.find()
    
    # Convertir los documentos a una lista
    documents_list = list(documents)
    
    # Guardar los documentos en un archivo JSON
    with open(output_file, 'w') as file:
        json.dump(documents_list, file, default=str)

    print(f"Colección '{collection_name}' exportada a '{output_file}'.")

    
def json_to_csv(json_file_path, csv_file_path):
    """
    Convierte un archivo JSON a CSV.

    Args:
        json_file_path (str): La ruta del archivo JSON.
        csv_file_path (str): La ruta donde se guardará el archivo CSV.
    """
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        df = pd.DataFrame(data)
        df.to_csv(csv_file_path, index=False)   