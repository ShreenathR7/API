import requests

api_url = "https://retail.logimaxindia.com/etail_v3/admin/index.php/admin_ret_dashboard_api/get_Sales_glance"

payload_data  = {
    "id_branch": "0",
    "from_date": "2000-7-29",
    "to_date": "2023-8-30"
}

try:
    response = requests.post(api_url, data=payload_data)

    # Check if the API request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Print the API response data
        print("API Response Data:")
        print(response_data)
    else:
        print(f"API Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"API Request failed with error: {e}")
