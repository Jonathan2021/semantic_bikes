from urllib.parse import quote

class Station:
    def __init__(self):
        self._name = None
        self._id = None
        self._lattitude = None
        self._longitude = None
        self._available = None
        self._free = None
        self._total = None
        self._cardPaiement = None
    
    def getName(self, doquote=True):
        return quote(self._name.encode("utf-8")) if isinstance(self._name, str) and doquote else self._name

    def setName(self, name):
        self._name = name

    def getId(self, doquote=True):
        return quote(self._id.encode("utf-8")) if isinstance(self._id, str) and doquote else self._id

    def setId(self, _id):
        self._id = _id

    def getLattitude(self, doquote=True):
        return quote(self._lattitude.encode("utf-8")) if isinstance(self._lattitude, str) and doquote else self._lattitude

    def setLattitude(self, lattitude):
        self._lattitude = lattitude

    def getLongitude(self, doquote=True):
        return quote(self._longitude.encode("utf-8")) if isinstance(self._longitude, str) and doquote else self._longitude

    def setLongitude(self, longitude):
        self._longitude = longitude

    def getAvailable(self, doquote=True):
        return quote(self._available.encode("utf-8")) if isinstance(self._available, str) and doquote else self._available

    def setAvailable(self, available):
        self._available = available
    
    def getFree(self, doquote=True):
        return quote(self._free.encode("utf-8")) if isinstance(self._free, str) and doquote else self._free

    def setFree(self, free):
        self._free = free

    def getTotal(self, doquote=True):
        return quote(self._total.encode("utf-8")) if isinstance(self._total, str) and doquote else self._total

    def setTotal(self, total):
        self._total = total

    def getCardPaiement(self, doquote=True):
        return quote(self._cardPaiement.encode("utf-8")) if isinstance(self._cardPaiement, str) and doquote else self._cardPaiement

    def setCardPaiement(self, cardPaiement):
        self._cardPaiement = cardPaiement
