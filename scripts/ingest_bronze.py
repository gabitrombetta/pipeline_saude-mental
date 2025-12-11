# %%
from dotenv import load_dotenv
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
        dataset='abdullahashfaqvirk/student-mental-health-survey',
        file_name='MentalHealthSurvey.csv',
        path=f'../{PATH}'
    )

    print(f'[INFO] Arquivo salvo em {PATH} na data {date_today}')
except Exception as e:
    print(f'[WARN] Erro ao salvar: {e}')
