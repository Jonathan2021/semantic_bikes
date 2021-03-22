# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
import pickle
import numpy as np
import json
import urllib.request
from math import sin, cos, sqrt, atan2, radians
from pyfuseki import FusekiUpdate, FusekiQuery

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/route")
def route():
    return render_template("route.html",title='Route Finder')

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
    print(data)
    if len(zip)==5:
        dpt=zip[:2]
    else:
        dpt=zip[:1]
    fuseki_query=FusekiQuery('http://127.0.0.1:3030','ds')
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


def getGeoloc(address):
    connect="http://api.positionstack.com/v1/forward?access_key=9b0ba3fad0620bd25e100ce2dfbd1627&country=FR&limit=1&results=latitude,longitude&query="
    connect=connect+address
    print(connect)
    with urllib.request.urlopen(connect) as url:
        data = json.loads(url.read().decode())
    return {'latitude':data['data'][0]['latitude'],'longitude':data['data'][0]['longitude']}

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

@app.route('/route/itinerary',methods=['POST'])
def itinerary():
    features=[x for x in request.form.values()]
    addressFrom=features[0]+", "+features[1]
    addressTo=features[2]+", "+features[3]
    dataFrom=getGeoloc(addressFrom.replace(' ','%20'))
    dataTo=getGeoloc(addressTo.replace(' ','%20'))

    print('dataFrom')
    print(dataFrom)
    print('dataTo')
    print(dataTo)
    distance=getDistance(dataFrom['latitude'],dataFrom['longitude'],dataTo['latitude'],dataTo['longitude'])
    print(distance)
    

    return render_template("itinerary.html",title='Your Itinerary',distance=np.round(distance,1),addressFrom=addressFrom,addressTo=addressTo)

if __name__ == "__main__":
    app.run(debug=True)