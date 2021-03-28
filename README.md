##### WEB DATA MINING PROJECT : FIND ROUTE API #####

To install and run: `make env`, then `make` or `make all`.

##### REQUIREMENTS #####
The project has been developed in Python and is connected to the Fuseki API. Python with libraries pyfuseki, rdflib, numpy, json and flask have to be installed.
You can do so with `pip install -r requirements.txt` (or `make install`) or `pipenv install` (in the root with Pipfile) + `pipenv shell` (or `make env`).

You also have to install the fuseki-server triplestore manager. You can do so from [here](https://jena.apache.org/download/)

##### RUN THE PROJECT #####
To run the project, you have to run the flask project and the fuseki server.
You can do so by running `make run` or `make`.

##### RUNNING FLASK SERVER #####
To run the flask server, move to the folder WebApp Flask and run the command line `python app.py` from the *WebApp Flask* directory. The server will be running locally, using the port 5000. (http://127.0.0.1:5000).
You can also just do `make app`.

##### RUNNING FUSEKI SERVER #####
For seek of simplicity and to be able to run update HTTP queries, we have pushed on Github the whole database in the folder Data/tripleStore. You can also find the turtle file that we have used to create this database in the folder Data. 
To run the Apache Fuseki server, you’ll launch the server, allowing update queries on the database folder location using the following command line: 

`fuseki-server - -loc=”$PWD/Data/tripleStore” - - update /database`

Note that `$PWD` is the path to the root of the repo. Note also that it is very important to use the parameter - - update and the same database name (/database) to be able to run all HTTP queries properly. 
You can also simply use `make fuseki`.
