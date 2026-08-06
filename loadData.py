import os
import json
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

def transform_data(data) -> list[dict]:
    df = pd.DataFrame(data)
    df1 = df.copy()

    df1['bandwidth_usage_mbps'] = df1['bandwidth_usage_mbps'].astype('float32')
    df1['latency_ms'] = df1['latency_ms'].astype('float32')
    df1['packet_loss_percent'] = df1['packet_loss_percent'].astype('float32')

    df1['timestamp'] = pd.to_datetime(df1['timestamp'], format='ISO8601').dt.strftime('%Y-%m-%d %H:%M:%S').astype('string')
    df1['source_ip'] = df1['source_ip'].astype('string')
    df1['destination_ip'] = df1['destination_ip'].astype('category')

    data_cleaned = df1.to_dict(orient='records')
    return data_cleaned

def load_data(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def connect_to_supabase() -> Client:
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

if __name__ == "__main__":
    supabase = connect_to_supabase()
    data_network = load_data("network_log.json")
    cleaned_data = transform_data(data_network)
    try:
      pst = (
          supabase.table("network_log").insert(cleaned_data).execute()
      )
      print("Successfully load the data!")
    except Exception as e:
      print("Error:", e)
