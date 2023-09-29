import requests

api_url = 'http://13.126.240.225/lmxtrade/winbullliteapi/api/v1/wlclientsrates'
data = {"client": "kjpl"}

response = requests.post(api_url, json=data)

# Check the response status code and content
if response.status_code == 200:
    print("API call successful!")
    print("Response data:")
    print(response.json())
else:
    print(f"API call failed with status code: {response.status_code}")
    print("Error message:")
    print(response.text)
