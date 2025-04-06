import requests
import json
import time
from datetime import datetime

def send_test_data():
    # Test cases
    test_data = [
        {
            "packet_size": 1024,
            "protocol": "TCP",
            "source_ip": "192.168.1.100",
            "destination_ip": "192.168.1.1",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "packet_size": 4096,
            "protocol": "UDP",
            "source_ip": "192.168.1.104",
            "destination_ip": "192.168.1.1",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "packet_size": 896,
            "protocol": "TCP",
            "source_ip": "192.168.1.106",
            "destination_ip": "192.168.1.1",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "packet_size": 1024,
            "protocol": "TCP",
            "source_ip": "192.168.1.100"
        }
    ]

    print("Sending test network traffic data...")
    
    for data in test_data:
        try:
            # Send to API
            response = requests.post(
                "http://localhost:8050/predict",
                json=data
            )
            
            # Get result
            result = response.json()
            print(f"\nSent traffic data:")
            print(f"Protocol: {data['protocol']}")
            print(f"Packet size: {data['packet_size']}")
            print(f"Source IP: {data['source_ip']}")
            print(f"Result: {'Attack' if result['prediction'] == 1 else 'Normal'}")
            print("-" * 50)
            
            # Wait 2 seconds between requests
            time.sleep(2)
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    send_test_data() 