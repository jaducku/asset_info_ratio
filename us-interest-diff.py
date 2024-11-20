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
df = fdr.DataReader('FRED:T10Y2Y',today)

data= {
    "date": str(today),
    "value": df.iloc[0]['T10Y2Y'],
}

load_dotenv()

# Supabase URL과 API Key 가져오기
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")

# Supabase 클라이언트 생성
supabase: Client = create_client(supabase_url, supabase_key)

try:
    response = supabase.schema('economy').table("us_sl_interest_rate_diff").insert(data).execute()
except Exception as e:
    print("오류 발생:", e)
