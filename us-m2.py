import FinanceDataReader as fdr
import pandas as pd
from datetime import date,timedelta
from supabase import create_client, Client
from dotenv import load_dotenv
import json
import os
import pandas as pd
from math import isnan

# M2 파싱해올곳이 없음