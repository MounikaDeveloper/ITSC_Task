import requests
try:
    result = requests.get("http://127.0.0.1:8000/datetime/")
    json_response=result.json()
    print(json_response)
except requests.ConnectionError:
    print("server not available")
