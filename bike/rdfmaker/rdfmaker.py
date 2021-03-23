import sys
import os
import errno
sys.path.append('..')
from consts import consts
from rdflib.namespace import RDF, RDFS, XSD
from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.plugins.stores import sparqlstore


class RdfMaker:
    @staticmethod
    def generateRDF(city, tofuseki=False):
        
        ex = Namespace("http://www.example.com/")
        geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
        dbo = Namespace("http://dbpedia.org/ontology/")
        dbr = Namespace("http://dbpedia.org/resource/")


        g = Graph()

        city_prop = dbo.city
        type_prop = RDF.type
        country_prop = dbo.country
        label_prop = RDFS.label
        bikestation_prop = ex.bikeStation
        bikestation_uris = [URIRef(ex + city.getName() + str(i)) for i in range(len(city.getStations()))]

        bicycle_sharing_entity = URIRef(dbr + "Bicycle-sharing_system")
        
        available_prop = ex.available
        free_prop = ex.free
        total_prop = ex.total
        cardPaiement_prop = ex.cardPaiement
        lat_prop = geo.lat
        long_prop = geo.long

        city_ressource = URIRef(dbr + city.getName())
        city_name = Literal(city.getName())

        g.namespace_manager.bind("ex", ex)
        g.namespace_manager.bind("geo", geo)
        g.namespace_manager.bind("dbo", dbo)
        g.namespace_manager.bind("dbr", dbr)

        for station_uri, station in zip(bikestation_uris, city.getStations()):
            g.add((station_uri, type_prop, bicycle_sharing_entity))
            g.add((station_uri, city_prop, city_ressource))
            if station.getName() is not None:
                g.add((station_uri, label_prop, Literal(station.getName())))

            if station.getLongitude() is not None:
                g.add((station_uri, long_prop, Literal(station.getLongitude())))

            if station.getLattitude() is not None:
                g.add((station_uri, lat_prop, Literal(station.getLattitude())))

            if station.getAvailable() is not None:
                g.add((station_uri, available_prop, Literal(station.getAvailable())))
        
            if station.getTotal() is not None:
                g.add((station_uri, total_prop, Literal(station.getTotal())))
            
            if station.getFree() is not None:
                g.add((station_uri, free_prop, Literal(station.getFree())))

            if station.getCardPaiement() is not None:
                g.add((station_uri, cardPaiement_prop, Literal(station.getCardPaiement())))
            else:
                g.add((station_uri, cardPaiement_prop, Literal(False)))
            
        path = consts.turtle_dir + city.getName(doquote=False) + ".ttl"

        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        g.serialize(destination=path, format="turtle")

        if tofuseki:
            query_endpoint = consts.triplestore + '/query'
            update_endpoint =  consts.triplestore + '/update'
            store = sparqlstore.SPARQLUpdateStore()
            store.open((query_endpoint, update_endpoint))
            
            identifier = URIRef(ex + city.getName())
            ng = Graph(store, identifier=identifier)
            ng.update(

                    u'INSERT DATA { %s }' % g.serialize(format='turtle').decode("utf-8")
            )
