import xml.etree.ElementTree as ET
import sys
sys.path.append('..')
from models.city import City
from models.station import Station
from rdfmaker.rdfmaker import RdfMaker
from .helper.helper import get_url_content

class XmlParser:
        def parse(url, cityName, country):
            root = ET.fromstring(get_url_content(url))
            
            city = City();
            city.setName(cityName);
            city.setCountry(country);
            
            elements = root[0]

            for element in elements:
                station = Station()
                properties = element.attrib

                station.setName(properties.get('na'))
                st_id = properties.get('id')
                station.setId(int(st_id) if st_id else st_id)
                lat = properties.get('la')
                station.setLattitude(float(lat) if lat else lat)
                lon = properties.get('lg')
                station.setLongitude(float(lon) if lon else lon)
                total = properties.get('to')
                station.setTotal(int(total) if total else total)
                avail = properties.get('av')
                station.setAvailable(int(avail) if avail else avail)
                free = properties.get('fr')
                station.setFree(int(free) if free else free)

                city.addStation(station)

            RdfMaker.generateRDF(city)
