'''
Class that handles all internal API calls

Attributes:
    base_url: string of base url of client
    api_key: key used to access the information

Functions:
    build_url: builds the url to get an endpoint to retrieve data
    get: returns the json of the information
'''
import httpx
from urllib.parse import urljoin
from typing import Dict

class InternalAPIClient:
    def __init__(self, base_url: str, api_key: str, add_headers: Dict[str, str] = None):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"}

        if (add_headers):
            for key, value in add_headers:
                self.headers[key] = value
    
    def build_url(self, path: str) -> str:
        '''
        Builds a full url to reach endpoint for data.

        Parameters:
            path(str): path to endpoint

        Result:
            str: full url
        '''
        return urljoin(self.base_url, path)
    
    async def get(self, path: str, params: dict = None):
        '''
        Retrieves the data from specified endpoint.

        Parameters:
            path(str): path to endpoint
            params(dict): any parameters needed for json response
        
        Result:
            dict: json of data requested
        '''
        url = self.build_url(path)
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()