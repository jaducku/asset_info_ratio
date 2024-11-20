import FinanceDataReader as fdr
import pandas as pd
from datetime import date,timedelta
from supabase import create_client, Client
from dotenv import load_dotenv
import json
import os
import pandas as pd
from math import isnan

'''
us_dow = fdr.DataReader('DJI')
us_nasdaq = fdr.DataReader('IXIC')
us_snp500 = fdr.DataReader('S&P500')

datas_dow= []
datas_nasdaq= []
datas_snp500= []

for item in us_dow.itertuples():
    data1 = {
        "date": str(item[0]),
        "value": item[4]
    }
    datas_dow.append(data1)

for item in us_nasdaq.itertuples():
        
    data2 = {
        "date": str(item[0]),
        "value": item[4]
    }
    datas_nasdaq.append(data2)

for item in us_snp500.itertuples():
        
    data3 = {
        "date": str(item[0]),
        "value": item[4]
    }
    datas_snp500.append(data3)


load_dotenv()

# Supabase URL과 API Key 가져오기
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")

# Supabase 클라이언트 생성
supabase: Client = create_client(supabase_url, supabase_key)

try:
    response = supabase.schema('economy').table("us_dow").insert(datas_dow).execute()
    response = supabase.schema('economy').table("us_nasdaq").insert(datas_nasdaq).execute()
    response = supabase.schema('economy').table("us_snp500").insert(datas_snp500).execute()
except Exception as e:
    print("오류 발생:", e)
'''
#일간 작업

today = str(date.today() - timedelta(days=1))#str(date.today()) 

dow_value = round(fdr.DataReader('DJI',today).loc[today, 'Close'],2)
nasdaq_value = round(fdr.DataReader('IXIC',today).loc[today, 'Close'],2)
snp500_value = round(fdr.DataReader('S&P500',today).loc[today, 'Close'],2)

data_dow= {
    "date": str(today),
    "value": dow_value
}

datas_nasdaq= {
    "date": str(today),
    "value": nasdaq_value
}

data_snp500= {
    "date": str(today),
    "value": snp500_value
}

load_dotenv()

# Supabase URL과 API Key 가져오기
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")

# Supabase 클라이언트 생성
supabase: Client = create_client(supabase_url, supabase_key)

try:
    response = supabase.schema('economy').table("us_dow").insert(datas_dow).execute()
    response = supabase.schema('economy').table("us_nasdaq").insert(datas_nasdaq).execute()
    response = supabase.schema('economy').table("us_snp500").insert(datas_snp500).execute()
    
except Exception as e:
    print("오류 발생:", e)