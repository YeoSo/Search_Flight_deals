import requests
from pprint import pprint

endpoint = ""


class DataManager:

    def __init__(self):
        self.response = requests.get(url=endpoint)
        self.data = self.response.json()['prices']

    def update_codes(self):
        for city in self.data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)


# data = DataManager().data

# pprint(data)
