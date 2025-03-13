import json
from utils import fetch_data, send_to_kafka
import threading

def produce_data():
    threading.Timer(30, produce_data).start()
    response  = fetch_data()
    data = json.loads(response.text)
    send_to_kafka(data)
    
    
if __name__ == "__main__":
    produce_data()