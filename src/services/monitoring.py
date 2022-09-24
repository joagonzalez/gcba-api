from prometheus_client import Summary, Gauge, Histogram, Counter

class Monitoring:
    def __init__(self):
        # Create a metric to track time spent and requests made.
        self.ecobici_station = Gauge('ecobici_station', 'GCBA Ecobici station information',
                                     labelnames=['id', 'capacity', 'lat', 'lon', 'name'])
        self.ecobici_amount_stations = Gauge('ecobici_amount_stations', 'Amount of available Ecobici Stations',
                                             )
        self.ecobici_bikes_capacity = Gauge('ecobici_bikes_capacity', 'Total capacity taking into account all avaliable stations')

        
monitor = Monitoring()