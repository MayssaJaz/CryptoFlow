import os
from kafka import KafkaProducer
import requests
from constants import fetch_data_url 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
kafka_server = os.getenv("KAFKA_SERVER")

def fetch_data():
    """
    Fetches cryptocurrencies details from the remote API.

    Returns:
        response (requests.Response): The response object from the GET request,
                                      which includes status code, headers, and content.
    """
    
    # Headers with compression and authorization
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Fetch data request
        response = requests.request("GET", fetch_data_url, headers=headers)
        return response
    
    except Exception as e:
        return {"message": e.message}
        
        
def send_to_kafka(data):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    # Send data to a Kafka topic
    producer.send('crypto-topic', value=str(data).encode())
    producer.flush() 
    print("Data sent to Kafka")