from selenium import webdriver
import time

# Start a new Selenium WebDriver (in this case, Chrome)
driver = webdriver.Edge()

# Define the API endpoint and payload
api_url = "https://retail.logimaxindia.com/etail_v3/admin/index.php/admin_ret_dashboard_api/get_Sales_glance"
payload = {
    "id_branch": "2",
    "from_date": "2000-7-29",
    "to_date": "2023-8-29"
}

# Measure the response time
start_time = time.time()
driver.get(api_url)
end_time = time.time()

# Calculate the response time in seconds
response_time = end_time - start_time

# Print the response time
print(f"API Response Time: {response_time} seconds")

# Close the WebDriver
driver.quit()

