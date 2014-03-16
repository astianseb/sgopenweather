import urllib2
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError


BASE_OPENWEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q='
UNITS = 'metric'

class Weather:
    def __init__(self, location):
        self.url = BASE_OPENWEATHER_URL + location + '&mode=xml&units=' + UNITS

    def get_response(self):
        self.urlhandler = urllib2.urlopen(self.url)
        self.response = self.urlhandler.read()
        return self.response

    def is_response_valid(self, response):
        try:
            self.tree = ElementTree.fromstring(response)
            return True
        except ParseError:
            return False

    def make_tree(self):
        return ElementTree.fromstring(self.response)

    def get_location(self):
        for loc in self.tree.iter('city'):
            return loc.get('name')

    def get_temperature(self):
        for temp in self.tree.iter('temperature'):
            return temp.get('value')

    def get_temperature_min(self):
        for temp in self.tree.iter('temperature'):
            return temp.get('min')

    def get_temperature_min(self):
        for temp in self.tree.iter('temperature'):
            return temp.get('min')

    def get_temperature_max(self):
        for temp in self.tree.iter('temperature'):
            return temp.get('max')

    def get_humidity(self):
        for hum in self.tree.iter('humidity'):
            humidity = hum.get('value')
            unit = hum.get('unit')
            return humidity + unit

    def get_pressure(self):
        for pres in self.tree.iter('pressure'):
            pressure = pres.get('value')
            unit = pres.get('unit')
            return pressure + ' ' + unit
           
    def get_wind(self):
        for pres in self.tree.iter('wind'):
            for i in pres.iter('speed'):
                wind_v = i.get('value')
                wind_n = i.get('name')
            for i in pres.iter('direction'):
                wind_d = i.get('name')
        return wind_v + ' ' + wind_n + ' ' + wind_d
    
    def get_clouds(self):
        for clouds in self.tree.iter('clouds'):
            return clouds.get('name')

