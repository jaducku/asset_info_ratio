import requests
from bs4 import BeautifulSoup
import json
import os
from supabase import create_client, Client
from dotenv import load_dotenv

dollar_index=0
won_dollar_rate=0
won_yen_rate=0
won_yuan_rate=0
dollar_gold_rate=0
dollar_silver_rate=0
dollar_bit_rate=0
p2p_ratio: 1.07


url = 'https://finance.naver.com/marketindex/'

response = requests.get(url)

if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
    soup = BeautifulSoup(response.text, 'html.parser')  # 응답 받은 HTML 파싱
    exchange_list = soup.find('div',id='sInput')  # 파싱한 데이터에서 div 태그 내 news_list 클래스 내 데이터 저장
    usd = exchange_list.find('option',class_='selectbox-default')
    won_dollar_rate = usd['value']
else:
    print('error')  # 오류 시 메시지 출력

url2 = 'https://www.kitco.com/charts/gold'
response = requests.get(url2)

if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
    soup = BeautifulSoup(response.text, 'html.parser')  # 응답 받은 HTML 파싱
    material_list = soup.find('script',id='__NEXT_DATA__').text
    json_data = json.loads(material_list)
    internal_gold_price_ozt = json_data['props']['pageProps']['dehydratedState']['queries'][1]['state']['data']['GetMetalQuoteV3']['results'][0]['ask']
    dollar_gold_rate = internal_gold_price_ozt
else:
    print('error')  # 오류 시 메시지 출력

url3 = 'https://www.kitco.com/charts/silver'
response = requests.get(url3)

if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
    soup = BeautifulSoup(response.text, 'html.parser')  # 응답 받은 HTML 파싱
    material_list = soup.find('script',id='__NEXT_DATA__').text
    json_data = json.loads(material_list)
    internal_silver_price_ozt = json_data['props']['pageProps']['dehydratedState']['queries'][1]['state']['data']['GetMetalQuoteV3']['results'][0]['ask']
    dollar_silver_rate = internal_silver_price_ozt
else:
    print('error')  # 오류 시 메시지 출력

load_dotenv()

# Supabase URL과 API Key 가져오기
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")

# Supabase 클라이언트 생성
supabase: Client = create_client(supabase_url, supabase_key)

# 삽입할 데이터
data = {
    "dollar_index": dollar_index,
    "won_dollar_rate": won_dollar_rate,
    "won_yen_rate": won_yen_rate,
    "won_yuan_rate": won_yuan_rate,
    "dollar_gold_rate": dollar_gold_rate,
    "dollar_silver_rate": dollar_silver_rate,
    "dollar_bit_rate": dollar_bit_rate,
    "p2p_ratio": 1.07
}

# 데이터 삽입
try:
    response = supabase.schema('assets').table("exchange_rate").insert(data).execute()
    print(response)
except Exception as e:
    print("오류 발생:", e)