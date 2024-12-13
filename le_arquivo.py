import pandas as pd
import os
from pathlib import Path


arquivos = [i for i in os.listdir(Path(__file__).parent / "data") if i[-5:] == '.json']
arquivo_json = [pd.read_json(Path(__file__).parent / "data" / arquivo) for arquivo in arquivos]
df_final = pd.concat([arquivo for arquivo in arquivo_json]).reset_index(drop=True)
print(df_final)
