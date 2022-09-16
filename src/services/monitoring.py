from prometheus_client import Summary, Gauge, Histogram, Counter

class Monitoring:
    def __init__(self):
        # Create a metric to track time spent and requests made.
        self.ecobici_station = Gauge('ecobici_station', 'GCBA Ecobici station information',
                                     labelnames=['id', 'capacity', 'lat', 'lon', 'name'])
        self.ecobici_amount_stations = Gauge('ecobici_amount_stations', 'Amount of available Ecobici Stations',
                                             )

        
monitor = Monitoring()