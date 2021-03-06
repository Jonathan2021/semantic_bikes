import sys
sys.path.append('..')
from models.station import Station
import json

class JsonParser:
    @staticmethod
    def parse(content, city):
        js = json.loads(content)

        if 'name' in js.keys():
            JsonParser.parseV1(js, city)
        elif 'facet_groups' in js.keys():
            if 'decaux' in js['parameters']['dataset']:
                JsonParser.parseDecaux(js, city)
            else:
                JsonParser.parseV3(js, city)
        elif 'records' in js.keys():
            JsonParser.parseV2(js, city)
        elif 'data' in js.keys():
            JsonParser.parseV5(js, city)
        else:
            JsonParser.parseV4(js, city)

    @staticmethod
    def parseV1(js, city):

        for feature in js['features']:
            properties = feature['properties']
            station = Station()
            station.setName(properties.get('name'))
            st_id = properties.get('number')
            station.setId(int(st_id) if st_id else st_id)
            lat = properties.get('lat')
            station.setLattitude(float(lat) if lat else lat)
            lon = properties.get('lng')
            station.setLongitude(float(lon) if lon else lon)
            total = properties.get('bike_stands')
            station.setTotal(int(total) if total else total)
            avail = properties.get('available_bikes')
            station.setAvailable(int(avail) if avail else avail)
            free = properties.get('available_bike_stands')
            station.setFree(int(free) if free else free)
            card = properties.get('banking')
            station.setCardPaiement(card == "true" if card else card)


            city.addStation(station);

    @staticmethod
    def parseV2(js, city):

        for record in js['records']:
            properties = record['fields']
            station = Station()

            station.setName(properties.get('nom'))
            st_id = properties.get('idstation')
            station.setId(int(st_id) if st_id else st_id)
            coords = properties.get('coordonnees')
            if coords:
                station.setLattitude(float(coords[0]))
                station.setLongitude(float(coords[1]))
            total = properties.get('nombreemplacementsactuels')
            station.setTotal(int(total) if total else total)
            avail = properties.get('nombrevelosdisponibles')
            station.setAvailable(int(avail) if avail else avail)
            free = properties.get('nombreemplacementsdisponibles')
            station.setFree(int(free) if free else free)

            city.addStation(station);

    @staticmethod
    def parseV3 (js, city):

        for record in js['records']:
            properties = record['fields']
            station = Station()

            station.setName(properties.get('name'))
            station.setId(properties.get('recordid'))
            coords = properties.get('geo_point_2d')
            if coords:
                station.setLattitude(float(coords[1]))
                station.setLongitude(float(coords[0]))
            total = properties.get('capacity')
            station.setTotal(int(total) if total else total)
            
            city.addStation(station);

    def parseV4(js, city):
        for feature in js['features']:
            properties = feature['properties']
            station = Station()

            voie = properties.get('NOM_VOIE')
            voie = "" if not voie else voie
            compl = properties.get("COMPL_LOC")
            compl = "" if not compl else compl
            name = voie +" "+ compl 
            station.setName(name if name != " " else None)

            st_id = feature.get('id')
            station.setId(int(st_id) if st_id else st_id)

            coords = feature.get('geometry')
            if coords and coords.get('coordinates'):
                coords = coords.get('coordinates')
                station.setLattitude(float(coords[1]))
                station.setLongitude(float(coords[0]))
            total = properties.get('NBR_PT_ACC')
            station.setTotal(int(total) if total else total)
            avail = properties.get('NBR_VELO')
            station.setAvailable(int(avail) if avail else avail)
            if total and avail:
                free = int(total) - int(avail)
                station.setFree(free)

            city.addStation(station);


    def parseDecaux(js, city):

        for record in js['records']:
            properties = record['fields']
            station = Station()

            station.setName(properties.get('name'))
            st_id = properties.get('number')
            station.setId(int(st_id) if st_id else st_id)

            coords = properties.get('position')
            if coords:
                station.setLattitude(float(coords[0]))
                station.setLongitude(float(coords[1]))
            
            total = properties.get('bike_stands')
            station.setTotal(int(total) if total else total)
            avail = properties.get('available_bikes')
            station.setAvailable(int(avail) if avail else avail)
            free = properties.get('available_bike_stands')
            station.setFree(int(free) if free else free)
            card = properties.get('banking')
            station.setCardPaiement(card != "False" if card else card)


            city.addStation(station);

    def parseV5(js, city):
        stations = js['data']['stations']
        for properties in stations:
            station = Station()
            station.setName(properties.get('name'))
            st_id = properties.get('station_id')
            station.setId(int(st_id) if st_id else st_id)
            lat = properties.get('lat')
            station.setLattitude(float(lat) if lat else lat)
            lon = properties.get('lon')
            station.setLongitude(float(lon) if lon else lon)
            total = properties.get('capacity')
            station.setTotal(int(total) if total else total)

            city.addStation(station);
