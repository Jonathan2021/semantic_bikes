# -*- coding: utf-8 -*-
import sys
sys.path.append('../bike')
sys.path.append('..')
from bike.main import parse
from flask import Flask,render_template,request
import pickle
import numpy as np
import json
import urllib.request
from math import sin, cos, sqrt, atan2, radians
from pyfuseki import FusekiUpdate, FusekiQuery

app = Flask(__name__, template_folder='templates')

def getGeoloc(address):
    connect="http://api.positionstack.com/v1/forward?access_key=9b0ba3fad0620bd25e100ce2dfbd1627&country=FR&limit=1&results=latitude,longitude&query="
    connect=connect+address
    print(connect)
    with urllib.request.urlopen(connect) as url:
        data = json.loads(url.read().decode())
    try:
        lat=data['data'][0]['latitude']
        long=data['data'][0]['longitude']
        return {'latitude':lat,'longitude':long}
    except:
        return None

def getDistance(lat1,lon1,lat2,lon2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def deleteTripleStore(city):
    query=FusekiUpdate('http://127.0.0.1:3030','bikes')
    sparql="""

    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/> 
    PREFIX ex: <http://www.example.com/> 
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    DELETE  { ?a ?p ?o}
    WHERE {
        ?a dbo:city dbr:"""+city+""" .
        ?a ?p ?o .
    }"""
    query.run_sparql(sparql)

def insertNewTriplestore(data):
    query=FusekiUpdate('http://127.0.0.1:3030','bikes')
    sparql="""
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/> 
    PREFIX ex: <http://www.example.com/> 
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    INSERT DATA  { """+data+"""}
    """
    query.run_sparql(sparql)

def updateTriplestore(city,data):
    print('Inside udpdate')
    deleteTripleStore(city)
    print('Delete Done')
    insertNewTriplestore(data)
    print('Insert Done')



@app.route("/")
def home():
    return render_template("home.html", title='Find Your Path API')

@app.route("/route")
def route():
    return render_template("route.html",title='Route Finder')

@app.route("/postoffices")
def postoffices():
    return render_template("postoffices.html",title='Post Offices Finder')

@app.route("/postoffices/found",methods=['POST'])
def postofficesFound():
    features=[x for x in request.form.values()]
    address = features[0]+', '+ features[1]
    distance=int(features[3])
    print('distance',distance)
    zip=features[2]
    address=address+' '+str(zip)
    data=getGeoloc(address.replace(' ','%20'))
    if data is None:
        return render_template("not_found.html",title='Oops !')
    print(data)
    if len(zip)==5:
        dpt=zip[:2]
    else:
        dpt=zip[:1]
    fuseki_query=FusekiQuery('http://127.0.0.1:3030','post_offices')
    sparql_str="PREFIX prop: <http://sample.com/prop/>\nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX type: <http://sample.com/type/>\n"
    sparql_str+="SELECT ?name ?ad ?city ?zip ?dpt ?lat ?long ?phone WHERE {?a rdf:type type:PostOffice . ?a prop:Name ?name . ?a prop:City ?city .?a prop:Zipcode ?zip .?a prop:Dpt \""+str(dpt)+"\"  .?a prop:Address ?ad .?a prop:Lattitude ?lat . ?a prop:Longitude ?long . ?a prop:Phone ?phone . }"
    query_result=fuseki_query.run_sparql(sparql_str)
    result=query_result.convert()
    print(result)
    result_final=[]
    for i in result['results']['bindings']:
        i["distance"]=np.round(getDistance(data['latitude'],data['longitude'],float(i['lat']['value']),float(i['long']['value'])),2)
        print(i["distance"])
        if float(i["distance"])<=float(distance):
            result_final.append(i)
    result_final.sort(key=lambda x:x['distance'])
    print(result_final)
    return render_template("postoffices_found.html",title='Found Post Offices',result_final=result_final)

@app.route("/libraries")
def libraries():
    return render_template("libraries.html",title='Libraries Finder')

@app.route("/libraries/found",methods=['POST'])
def librariesFound():
    features=[x for x in request.form.values()]
    address = features[0]+', '+ features[1]
    distance=int(features[3])
    print('distance',distance)
    zip=features[2]
    address=address+' '+str(zip)
    data=getGeoloc(address.replace(' ','%20'))
    if data is None:
        return render_template("not_found.html",title='Oops !')
    print(data)
    if len(zip)==5:
        dpt=zip[:2]
    else:
        dpt=zip[:1]
    fuseki_query=FusekiQuery('http://127.0.0.1:3030','libraries')
    sparql_str="PREFIX prop: <http://sample.com/prop/>\nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX type: <http://sample.com/type/>\n"
    sparql_str+="SELECT ?a ?name ?ad ?city ?zip ?dpt ?lat ?long WHERE {?a rdf:type type:Library . ?a prop:Name ?name . ?a prop:City ?city .?a prop:Zipcode ?zip .?a prop:Dpt \""+str(dpt)+"\"  .?a prop:Address ?ad .?a prop:Lattitude ?lat . ?a prop:Longitude ?long . }"
    query_result=fuseki_query.run_sparql(sparql_str)
    result=query_result.convert()
    print(result)
    result_final=[]
    for i in result['results']['bindings']:
        i["distance"]=np.round(getDistance(data['latitude'],data['longitude'],float(i['lat']['value']),float(i['long']['value'])),2)
        print(i["distance"])
        if float(i["distance"])<=float(distance):
            result_final.append(i)
    result_final.sort(key=lambda x:x['distance'])
    print(result_final)
    return render_template("libraries_found.html",title='Found Libraries',result_final=result_final)




@app.route('/route/itinerary',methods=['POST'])
def itinerary():
    features=[x for x in request.form.values()]
    addressFrom=features[0]+", "+features[2]
    addressTo=features[1]+", "+features[2]
    city=features[2]
    print(city)
    dataFrom=getGeoloc(addressFrom.replace(' ','%20'))
    dataTo=getGeoloc(addressTo.replace(' ','%20'))
    if dataFrom is None or dataTo is None:
        return render_template("not_found.html",title='Oops !')
    updateTriplestore(city,parse(city).split('\n',7)[7])
    print(dataFrom)
    print(dataTo)
    fuseki_query=FusekiQuery('http://127.0.0.1:3030','bikes')
    sparql_str="""
    PREFIX dbo: <http://dbpedia.org/ontology/> 
    PREFIX dbr: <http://dbpedia.org/resource/> 
    PREFIX ex: <http://www.example.com/> 
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    SELECT ?city ?label ?free ?available ?lat ?long
    WHERE { 
      
      ?a a dbr:Bicycle-sharing_system.
      ?a rdfs:label ?label .
      ?a ex:available ?available .
      ?a ex:free ?free .
      ?a geo:lat ?lat .
      ?a geo:long ?long .
      ?a dbo:city dbr:"""+city+""" .
    }
    """
    query_result=fuseki_query.run_sparql(sparql_str)
    result=query_result.convert()
    print(result)
    result_depart=None
    result_arrivee=None
    for i in result['results']['bindings']:
        distance_depart=np.round(getDistance(dataFrom['latitude'],dataFrom['longitude'],float(i['lat']['value']),float(i['long']['value'])),2)
        distance_arrivee=np.round(getDistance(dataTo['latitude'],dataTo['longitude'],float(i['lat']['value']),float(i['long']['value'])),2)
        if result_depart==None :
            if int(i['available']['value'])>0:
                result_depart=i
                result_depart['distance']=distance_depart
        elif result_depart['distance']>distance_depart and int(i['available']['value'])>0:
            result_depart=i
            result_depart['distance']=distance_depart

        if result_arrivee==None :
            if int(i['free']['value'])>0:
                result_arrivee=i
                result_arrivee['distance']=distance_arrivee
        elif result_arrivee['distance']>distance_arrivee and int(i['free']['value'])>0:
            result_arrivee=i
            result_arrivee['distance']=distance_arrivee

    print(result_depart)
    print(result_arrivee)
    distance_totale=np.round(getDistance(dataFrom['latitude'],dataFrom['longitude'],dataTo['latitude'],dataTo['longitude']),2)
    if result_depart== None or result_arrivee==None or (float(result_depart['lat']['value'])==float(result_arrivee['lat']['value']) and float(result_depart['long']['value'])==float(result_arrivee['long']['value'])):
        found=False
        print(found)
        return render_template("itinerary.html",title='Your Itinerary',found=found,distance_totale=distance_totale,addressFrom=addressFrom,addressTo=addressTo)
    else:
        found=True
        print(found)
        distance_velo=np.round(getDistance(float(result_depart['lat']['value']),float(result_depart['long']['value']),float(result_arrivee['lat']['value']),float(result_arrivee['long']['value'])),2)
        return render_template("itinerary.html",title='Your Itinerary',distance_velo=distance_velo,distance_totale=distance_totale,addressFrom=addressFrom,addressTo=addressTo,
            found=found,result_depart=result_depart,result_arrivee=result_arrivee)

if __name__ == "__main__":
    app.run(debug=True)