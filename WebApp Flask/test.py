from pyfuseki import FusekiUpdate, FusekiQuery

with open('../Data/tripleStore.ttl','r') as f:
	a=f.read()

a=a.split('\n',10)[10]
print(a[:200])

query=FusekiUpdate('http://127.0.0.1:3030','database')
sparql="""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/> 
PREFIX ex: <http://www.example.com/>
PREFIX prop: <http://www.example.com/prop/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX type: <http://www.example.com/type/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
INSERT DATA  { ex:test rdf:type type:Babar}
"""
query.run_sparql(sparql)