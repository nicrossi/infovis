from datetime import datetime

import pandas as pd

def read_csv_file(file_path):
    """
    Reads a CSV file from the given file path and returns a pandas DataFrame.

    :param file_path: str, the path to the CSV file.
    :return: DataFrame, the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def export_df_to_csv(df, file_path):
    """
    Exports a pandas DataFrame to a CSV file at the specified file path.

    :param df: DataFrame, the pandas DataFrame to export.
    :param file_path: str, the path where the CSV file will be saved.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"DataFrame successfully saved to {file_path}")
    except Exception as e:
        print(f"Error exporting DataFrame to CSV: {e}")


def filter_data(df):
    # Convert 'fecha_vigencia' to datetime
    df['fecha_vigencia'] = pd.to_datetime(df['fecha_vigencia'], format='%d/%m/%Y %H:%M', errors='coerce')
    # Define start and end dates for filtering
    start_date = datetime.strptime('01/12/2023', '%d/%m/%Y')
    end_date = datetime.strptime('07/07/2024', '%d/%m/%Y')
    df_filtered = df[
        (df['producto'] == 'Nafta (súper) entre 92 y 95 Ron')
        & (df['empresabandera'] == 'YPF')
        & (df['fecha_vigencia'] >= start_date)
        & (df['fecha_vigencia'] <= end_date)
    ]
    # Selecting only the specified columns
    return df_filtered[['fecha_vigencia', 'precio', 'provincia', 'localidad', 'direccion']]


# Constants
FILENAME = 'precios-historicos'
INPUT_RAW_CSV = f'/Users/nick/workspace/infovis/final/{FILENAME}.csv'
OUTPUT_FILTERED_CSV = f'/Users/nick/workspace/infovis/final/{FILENAME}-filtered.csv'

if __name__ == '__main__':
    # Read the CSV file to panda DataFrame
    df = read_csv_file(INPUT_RAW_CSV)
    # Filter data
    df_filtered = filter_data(df)
    # Export filtered DataFrame to a new CSV file
    export_df_to_csv(df_filtered, OUTPUT_FILTERED_CSV)

