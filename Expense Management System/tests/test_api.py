import requests

API_URL = "http://localhost:8000"

response = requests.get(f"{API_URL}/monthly_summary/")
print("Status Code:", response.status_code)
print("Response:", response.text)
