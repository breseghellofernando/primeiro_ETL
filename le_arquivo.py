import pandas as pd
import os
from pathlib import Path

def extract_data(pasta: str, sufixo: str) -> pd.DataFrame:

    arquivos = [i for i in os.listdir(Path(__file__).parent / pasta) if i[-5:] == '.' + sufixo]
    arquivo_json = [pd.read_json(Path(__file__).parent / pasta / arquivo) for arquivo in arquivos]
    df_final = pd.concat([arquivo for arquivo in arquivo_json]).reset_index(drop=True)

    return df_final

def transform_data(df_: pd.DataFrame, coluna: str, new_col: str) -> pd.DataFrame:

    df_[new_col] = df_[coluna] * 10
    return df_

def load_data(df: pd.DataFrame, formato: list):

    for i in formato:
        if i == 'csv':
            df.to_csv(Path(__file__).parent / 'arquivo.csv', sep = ";", index = False)
        if i == 'parquet':
            df.to_parquet(Path(__file__).parent / 'arquivo.parquet')

