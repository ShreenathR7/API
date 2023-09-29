import requests
import time

api_url = "https://retail.logimaxindia.com/etail_v3/admin/index.php/admin_ret_dashboard_api/get_Sales_glance"

payload_data = {
    "id_branch": "0",
    "from_date": "2000-7-29",
    "to_date": "2023-8-30"
}

try:
    start_time = time.time()
    response = requests.post(api_url, data=payload_data)
    end_time = time.time()
    api_response = response.json()
   
    # Check if the API request was successful
    if response.status_code == 200:
        # Calculate and print the response time in seconds
        response_data = response.json()
        response_time = end_time - start_time
        print(f"API Response Time: {response_time:.4f} seconds")
        print("API Response Data:")
        print(response_data)

        # You can also parse and print the API response data here
        # response_data = response.json()
        # print(response_data)
    else:
        print(f"API Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"API Request failed with error: {e}")

