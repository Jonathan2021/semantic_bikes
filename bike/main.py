import sys
from consts import consts
from models.city import City
from models.station import Station
from parsers.parser import Parser
import argparse

toParse = {
    'France': {
        'Montpellier': "https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml",

        'Strasbourg': "http://velhop.strasbourg.eu/tvcstations.xml",

        'Lyon': "https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=1.1.0&outputformat=GEOJSON&request=GetFeature&typename=jcd_jcdecaux.jcdvelov&SRSNAME=urn:ogc:def:crs:EPSG::4171",

        'Rennes': "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel",

        'Avignon': "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel",

        'Nice': "http://opendata.nicecotedazur.org/data/storage/f/2014-05-13T08%3A20%3A37.361Z/velobleu.geojson",

        'Marseille': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=marseille",

        'Valence': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=valence",

        'Toulouse': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=toulouse",

        'Nantes': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=nantes",

        'Nancy': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=nancy",

        'Amiens': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=amiens",

        'Rouen': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=rouen",

        'Besancon': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=Cergy-Pontoise",

        'Creteil': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=creteil",

        'Cergy-Pontoise': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=Cergy-Pontoise",

        'Mulhouse': "https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=mulhouse",

        'Saint-Étienne': "https://saint-etienne-gbfs.klervi.net/gbfs/en/station_information.json"
        }
    }

def parse(city, country="France"):
    tmp = toParse.get(country)
    if not tmp:
        print(f"No such country as {country} is supported", file=sys.stderr)
    url = tmp.get(city)
    if not url:
        print(f"No such city as {city} is supported", file=sys.stderr)
    return Parser.parse(url, city, country)

def parseAll():
    for country, cities in toParse.items():
        for city, url in cities.items():
            yield Parser.parse(url, city, country)


def main():
    for res in parseAll():
        print(res)

if __name__ == "__main__":
    main()
