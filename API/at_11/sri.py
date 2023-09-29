
import requests


class Api_Testing:
   
    # Creating a Constructor
    def __init__(self, url):
        self.url = url


    # Fetch the API Status Code
    def api_status_code(self):
        response = requests.get(self.url)
        print(response.json())
        return response.status_code
        
   
    # Fetch the ID from API Server
    def Get_ID(self, id):
        response = requests.get(self.url)
        data = response.json()
        print(response.json())
        id = str(id)
        for data in data:
            if(data['id']==id):
                return int(data['id'])
                



