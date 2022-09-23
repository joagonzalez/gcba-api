import time
import pprint
from src.services.gcba import GCBA
from src.config.setting import config
from src.services.monitoring import monitor
from src.services.loggerService import logger
from prometheus_client import start_http_server


class Application():
    def __init__(self) -> None:
        self.pp = pprint.PrettyPrinter(indent=4)
        self.api = GCBA()
                
    def run(self) -> None:
        '''
        Trigger main application
        '''
        logger.info('Starting application...')
        start_http_server(config['MONITORING_PORT'])
        
        while True:
            self.update_metric()
            time.sleep(config['GCBA_API_SAMPLING_TIME'])
            
    def fech_station_data(self):
        logger.info(f'updating stations data...')
        self.station_info = self.api.get_station_information()
        self.station_status = self.api.get_station_status()
        
    def pretty(self, data):
        return self.pp.pprint(data)
    
    def logic(self, station_info, station_status):
        output = dict()
        for station in station_info['data']['stations']:
            output[station['station_id']] = station
            output[station['station_id']]['bikes_available'] = next(item['num_bikes_available'] for item in station_status['data']['stations'] if item["station_id"] == station['station_id'])
            
        return output
             
    def update_metric(self):
        self.fech_station_data()
        monitor.ecobici_amount_stations.set(len(self.station_info['data']['stations']))
        data = self.logic(self.station_info, self.station_status)
        for station_id, station in data.items():
            try:
                monitor.ecobici_station.labels(station_id, 
                                            station['capacity'],
                                            station['lat'],
                                            station['lon'],
                                            station['name'],
                                            ).set(station['bikes_available'])
            except Exception as e:
                logger.error(f'Error updating metric for station {station_id}. Error: {e}')
            