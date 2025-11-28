# %%
from dotenv import load_dotenv
from create_sample import create_sample
from datetime import date
import kaggle
import os

# %%
load_dotenv(dotenv_path='../.env')

# %%
PATH = os.getenv("BRONZE_PATH")
date_today = date.today()

try:
    kaggle.api.dataset_download_file(
        dataset='mahdimashayekhi/mental-health',
        file_name='mental_health_dataset.csv',
        path=f'../{PATH}'
    )

    print(f'[INFO] Arquivo salvo em {PATH} na data {date_today}')
except Exception as e:
    print(f'[WARN] Erro ao salvar: {e}')

# %%
try:
    create_sample(f'../{PATH}/mental_health_dataset.csv')
except Exception as e:
    print(f'Erro ao criar sample: {e}')
