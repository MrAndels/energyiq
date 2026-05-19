# Importar librerías para análisis de datos
import pandas as pd
import numpy as np

# Definir URL RAW del dataset en GitHub
url = "https://raw.githubusercontent.com/MrAndels/energyiq/refs/heads/main/data/raw/energy_dataset_reducido.csv"

# Cargar dataset desde GitHub
df = pd.read_csv(
    url,
    
    # Separador de columnas del CSV
    sep=";",
    
    # Evita problemas de memoria
    low_memory=False
)

# Mostrar primeras filas del dataset
print("Primeras 5 filas del DataFrame:")
print(df.head())

# Mostrar nombres de columnas
print("\nColumnas del dataset:")
print(df.columns)

# Mostrar información general
print("\nInformación del dataset:")
print(df.info())