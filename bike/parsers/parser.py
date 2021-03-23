import sys
sys.path.append('..')
from models.city import City
from models.station import Station
from rdfmaker.rdfmaker import RdfMaker
from .helper.helper import get_url_content
from .xmlparser import XmlParser
from .jsonparser import JsonParser

class Parser:
        def parse(url, cityName, country, tofuseki=False):
            city = City();
            city.setName(cityName);
            city.setCountry(country);

            content = get_url_content(url)
            if content[0] == ord('<'):
                XmlParser.parse(content, city)
            else:
                JsonParser.parse(content, city)
            
            RdfMaker.generateRDF(city, tofuseki)
