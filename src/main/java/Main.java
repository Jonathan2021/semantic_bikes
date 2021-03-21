package main;

import consts.Consts;
import parsers.CityParser;
import parsers.XmlParser;
import parsers.UserFilesParser;


import org.apache.jena.rdfconnection.RDFConnection;
import org.apache.jena.rdfconnection.RDFConnectionFactory;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        while (true) {
            try {
                Thread.sleep(9000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            /* Delete triplestore content before uploading new one */
            RDFConnection conn = RDFConnectionFactory.connect(Consts.triplestore);
            conn.delete();

            /* Parse CSV files from users */
            UserFilesParser fr = new UserFilesParser();
            String directory = System.getProperty("user.dir") + "/added-files";
            final File folder = new File(directory);
            List<String> files = new ArrayList();
            files = fr.getFolderFiles(folder);

            fr.csvParser(files);

            /* Parse bike station files */
            /* Montpellier - France */
            XmlParser xmlParser = new XmlParser();
            xmlParser.XMLFileParser("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml", "Montpellier", "France");

            /* Strasbourg - France */
            xmlParser.XMLFileParser("http://velhop.strasbourg.eu/tvcstations.xml", "Strasbourg", "France");

            /* Lyon - France */
            CityParser cityparser = new CityParser();
            cityparser.jsonParser("https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=1.1.0&outputformat=GEOJSON&request=GetFeature&typename=jcd_jcdecaux.jcdvelov&SRSNAME=urn:ogc:def:crs:EPSG::4171", "Lyon", "France");

            /* Rennes - France */
            cityparser.jsonParserV2("https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel", "Rennes", "France");

            /* Avignon - France */
            cityparser.jsonParserV3("https://data.opendatasoft.com/api/records/1.0/search/?dataset=osm-fr-stations-de-velo-en-libre-service%40babel&facet=network&facet=operator&facet=source", "Avignon", "France");

            /* Nice - France */
            cityparser.jsonParserV4("http://opendata.nicecotedazur.org/data/storage/f/2014-05-13T08%3A20%3A37.361Z/velobleu.geojson", "Nice", "France");

            /* Marseille - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=marseille", "Marseille", "France");

            /* Valence - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=valence", "Valence", "France");

            /* Toulouse - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=toulouse", "Toulouse", "France");

            /* Nantes - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=nantes", "Nantes", "France");

            /* Nancy - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=nancy", "Nancy", "France");

            /* Amiens - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=amiens", "Amiens", "France");

            /* Rouen - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=rouen", "Rouen", "France");

            /* Besancon - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=besancon", "Besancon", "France");

            /* Creteil - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=creteil", "Creteil", "France");

            /* Cergy-Pontoise - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=Cergy-Pontoise", "Cergy-Pontoise", "France");

            /* Mulhouse - France */
            cityparser.jcdecauxParser("https://public.opendatasoft.com/api/records/1.0/search/?dataset=jcdecaux_bike_data&facet=banking&facet=bonus&facet=status&facet=contract_name&refine.contract_name=mulhouse", "Mulhouse", "France");
        }
    }
}
