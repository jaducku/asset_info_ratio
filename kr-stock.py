import FinanceDataReader as fdr
import pandas as pd
from datetime import date,timedelta
from supabase import create_client, Client
from dotenv import load_dotenv
import json
import os
import pandas as pd
from math import isnan

today = str(date.today()) 

kr_kospi = fdr.DataReader('KS11',today)
kr_kosdaq = fdr.DataReader('KQ11',today)

data_kospi= {
    "date": str(today),
    "value": kr_kospi.iloc[0]['Close'],
    "market_cap": int(kr_kospi.iloc[0]['MarCap'])
}

data_kosdaq= {
    "date": str(today),
    "value": kr_kosdaq.iloc[0]['Close'],
    "market_cap": int(kr_kosdaq.iloc[0]['MarCap'])
}

print(data_kospi)
print(data_kosdaq)


load_dotenv()

# Supabase URL과 API Key 가져오기
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")

# Supabase 클라이언트 생성
supabase: Client = create_client(supabase_url, supabase_key)

try:
    response = supabase.schema('economy').table("kr_kospi").insert(data_kospi).execute()
    response = supabase.schema('economy').table("kr_kosdaq").insert(data_kosdaq).execute()
except Exception as e:
    print("오류 발생:", e)
