class Station:
    def __init__(self, name="", _id="", lattitude="", longitude="", available="", free="", total="", cardPaiement=""):
        self._name = name
        self._id = _id
        self._lattitude = lattitude
        self._longitude = longitude
        self._available = available
        self._free = free
        self._total = total
        self._cardPaiment = cardPaiement
    
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getId(self):
        return self._id

    def setId(self, _id):
        self._id = _id

    def getLattitude(self):
        return self._lattitude

    def setLattitude(lattitude):
        self._lattitude = lattitude

    def getLongitude(self):
        return self._longitude

    def setLongitude(self, longitude):
        self._longitude = longitude

    def getAvailable(self):
        return self._available

    def setAvailable(self, available):
        self._available = available
    
    def getFree(self):
        return self._free

    def setFree(self, free):
        self._free = free

    def getTotal(self):
        return self._total

    def setTotal(self, total):
        self._total = total

    def getCardPaiement(self):
        return self._cardPaiement

    def setCardPaiement(self, cardPaiement):
        self._cardPaiement = cardPaiement
