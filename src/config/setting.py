import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'GCBA_API_URL': os.getenv('GCBA_API_URL', 'https://datosabiertos-transporte-apis.buenosaires.gob.ar:443'), 
    'GCBA_API_CLIENT_ID': os.getenv('GCBA_API_CLIENT_ID',''),
    'GCBA_API_CLIENT_SECRET': os.getenv('GCBA_API_CLIENT_SECRET', ''), 
    'GCBA_API_SAMPLING_TIME': int(os.getenv('GCBA_API_SAMPLING_TIME', 10)),
    'GCBA_ECOBICI_STATION_INFORMATION': os.getenv('GCBA_ECOBICI_STATION_INFORMATION', '/ecobici/gbfs/stationInformation'),
    'GCBA_ECOBICI_STATION_STATUS': os.getenv('GCBA_ECOBICI_STATION_STATUS', '/ecobici/gbfs/stationStatus'),
    'MONITORING_PORT': os.getenv('MONITORING_PORT', 8000),
}