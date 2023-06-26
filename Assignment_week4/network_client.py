import os
import asyncio
import requests

class NetworkClient:
    def __init__(self, base):
        self.base = base
    
    async def get_data(self, endpoint):
        """
        Gets data from the DataProvider
        
        -------------------

        """
        # Gets the data from the server.
        url = os.path.join(self.base, endpoint)
        response = requests.get(url)
        await asyncio.sleep(2)
        return response.json()