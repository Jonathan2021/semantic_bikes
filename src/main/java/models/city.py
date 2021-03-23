from urllib.parse import quote

class City:
    def __init__(self, doquote=True):
        self._name = None
        self._country = None
        self._bikeStations = []

    def addStation(self, bikeStation):
        self._bikeStations.append(bikeStation)

    def getName(self, doquote=True):
        return quote(self._name.encode("utf-8")) if isinstance(self._name, str) and doquote else self._name

    def setName(self, name):
        self._name = name

    def getCountry(self, doquote=True):
        return quote(self._country.encode("utf-8")) if isinstance(self._country, str) and doquote else self._country
    
    def setCountry(self, country):
        self._country = country
    
    def getStations(self):
        return self._bikeStations
    
    def setStations(self, bikeStations):
        self._bikeStations = bikeStations
