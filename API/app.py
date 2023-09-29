import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
api_url = "http://13.126.240.225/lmxtrade/winbullliteapi/api/v1/wlclientsrates"
data = {"client": "kjpl"}
def perform_api_load_test(url, data):
    # Define the number of iterations you want for the load test
    num_iterations = 100
    
    # Initialize the web driver
    driver = webdriver.Chrome()  # Or any other webdriver you prefer

    # Perform API load test using Selenium
    for _ in range(num_iterations):
        start_time = time.time()
        
        # Make the API call using 'requests'
        response = requests.post(url, json=data)
        
        # Get the API response and process it (optional)
        if response.status_code == 200:
            api_response = response.json()
            print(api_response)  # You can add any further processing if needed
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken for API call: {elapsed_time:.2f} seconds")
        
        # Delay between successive API calls to simulate real load
        time.sleep(1)

    # Close the web driver once the load test is done
    driver.quit()

# Run the API load test
perform_api_load_test(api_url, data)
