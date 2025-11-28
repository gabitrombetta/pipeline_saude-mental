import os
import pandas as pd


def create_sample(path):
    file_name, extension = os.path.splitext(path)
    extension = extension.lower().strip()

    if extension == ".csv":
        df = pd.read_csv(path)
        df = df.sample(min(300, len(df)), random_state=42)
        df.to_csv(f"{file_name}_sample.csv", index=False)
        print("[INFO] Sample criado")

    elif extension == ".parquet":
        df = pd.read_parquet(path)
        df = df.sample(min(300, len(df)), random_state=42)
        df.to_parquet(f"{file_name}_sample.parquet", index=False)
        print("[INFO] Sample criado")

    else:
        print(f"[WARN] Extensão de arquivo não reconhecida: {extension}")
