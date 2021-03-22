class City:
    def __init__(self, name="", country="", bikeStations=[]):
        self._name = name
        self._country = country
        self._bikeStations = bikeStations

    def addStation(self, bikeStation):
        self._bikeStations.append(bikeStation)

    def getName(self):
        return self._name

    def setName(selfname):
        self._name = name

    def getCountry(self):
        return self._country
    
    def setCountry(selfcountry):
        self._country = country
    
    def getStations(self):
        return self._bikeStations
    
    def setStations(self, bikeStations):
        self._bikeStations = bikeStations
