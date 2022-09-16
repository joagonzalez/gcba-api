import requests
from src.config.setting import config
from src.services.loggerService import logger

class GCBA():
    def __init__(self):
        self.api = config['GCBA_API_URL']
        self.client_id = config['GCBA_API_CLIENT_ID']
        self.client_secret = config['GCBA_API_CLIENT_SECRET']
        
        
    def get_station_information(self):
        result = None
        
        try:
            result = requests.get(
                        url=self.api + config['GCBA_ECOBICI_STATION_INFORMATION'],
                        params={'client_id': self.client_id, 'client_secret': self.client_secret}
            )
        except Exception as e:
            logger.error(f'Error getting station information. Error: {e}')
            
        return result.json()
    
    def get_station_status(self):
        result = None
        
        try:
            result = requests.get(
                        url=self.api + config['GCBA_ECOBICI_STATION_STATUS'],
                        params={'client_id': self.client_id, 'client_secret': self.client_secret}
            )
        except Exception as e:
            logger.error(f'Error getting station information. Error: {e}')
            
        return result.json()