import requests
import concurrent.futures
api_url = "https://retail.logimaxindia.com/etail_v3/admin/index.php/admin_ret_dashboard_api/get_Sales_glance"
data = {"id_branch": "1",
    "from_date": "2000-7-29",
    "to_date": "2023-8-29"}
def make_api_request(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        api_response = response.json()
        return api_response
    else:
        return None

def perform_concurrent_api_load_test(url, data, num_users):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_users) as executor:
        future_to_response = {executor.submit(make_api_request, url, data): i for i in range(num_users)}

        for future in concurrent.futures.as_completed(future_to_response):
            user_id = future_to_response[future]
            try:
                api_response = future.result()
                if api_response:
                    print(f"User {user_id}: {api_response}")
            except Exception as e:
                print(f"User {user_id}: Error occurred: {e}")

# Number of concurrent users for the load test
num_users = 10000

# Run the concurrent API load test
perform_concurrent_api_load_test(api_url, data, num_users)



