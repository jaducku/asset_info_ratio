import FinanceDataReader as fdr
import pandas as pd
from datetime import date,timedelta
from supabase import create_client, Client
from dotenv import load_dotenv
import json
import os
import pandas as pd
from math import isnan

df = fdr.DataReader('CPI','1''2024')

datas= []

for item in df.itertuples():
    value=0
    if(not isnan(item[4])):
        value = item[4]
        
    data = {
        "created_at": str(item[0]),
        "value": value
    }
    datas.append(data)

load_dotenv()

# Supabase URL과 API Key 가져오기
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")

# Supabase 클라이언트 생성
supabase: Client = create_client(supabase_url, supabase_key)

try:
    response = supabase.schema('economy').table("cpi").insert(datas).execute()
except Exception as e:
    print("오류 발생:", e)
