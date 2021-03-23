from consts import consts
from models.city import City
from models.station import Station
from parsers.xmlparser import XmlParser
from parsers.jsonparser import JsonParser

def parseAll():
        XmlParser.parse("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml", "Montpellier", "France")

        # Strasbourg - France 
        XmlParser.parse("http://velhop.strasbourg.eu/tvcstations.xml", "Strasbourg", "France")

        # Lyon - France 
        JsonParser.parse("https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=1.1.0&outputformat=GEOJSON&request=GetFeature&typename=jcd_jcdecaux.jcdvelov&SRSNAME=urn:ogc:def:crs:EPSG::4171", "Lyon", "France")

        # Rennes - France 
        JsonParser.parseV2("https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel", "Rennes", "France")

        # Avignon - France 
        JsonParser.parseV3("https://data.opendatasoft.com/api/records/1.0/search/?dataset=osm-fr-stations-de-velo-en-libre-service%40babel&facet=network&facet=operator&facet=source", "Avignon", "France")

        # Nice - France 
        JsonParser.parseV4("http://opendata.nicecotedazur.org/data/storage/f/2014-05-13T08%3A20%3A37.361Z/velobleu.geojson", "Nice", "France")

        # Marseille - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=marseille", "Marseille", "France")

        # Valence - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=valence", "Valence", "France")

        # Toulouse - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=toulouse", "Toulouse", "France")

        # Nantes - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=nantes", "Nantes", "France")

        # Nancy - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=nancy", "Nancy", "France")

        # Amiens - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=amiens", "Amiens", "France")

        # Rouen - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=rouen", "Rouen", "France")

        # Besancon - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=besancon", "Besancon", "France")

        # Creteil - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=creteil", "Creteil", "France")

        # Cergy-Pontoise - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=Cergy-Pontoise", "Cergy-Pontoise", "France")

        # Mulhouse - France 
        JsonParser.parse("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=mulhouse", "Mulhouse", "France")

        # Saint-Étienne - France
        JsonParser.parse("https://saint-etienne-gbfs.klervi.net/gbfs/en/station_information.json", "Saint-Étienne", "France")

if __name__ == "__main__":
    parseAll()
