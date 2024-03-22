import logging

import requests as requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.hub_gateway import HubGateway

import json
from datetime import datetime


class HubHttpAdapter(HubGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_data: ProcessedAgentData):
        url = f'{self.api_base_url}/processed_agent_data'

        def default_converter(o):
            if isinstance(o, datetime):
                return o.isoformat()
            raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

        data_json = json.dumps(processed_data.dict(), default=default_converter)

        response = requests.post(url, data=data_json)

        if response.status_code != 200:
            logging.info(f"Invalid Hub response\nData: {data_json}\nResponse: {response}")
            return False
        return True
