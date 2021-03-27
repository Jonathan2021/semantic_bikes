##### WEB DATA MINING PROJECT : FIND ROUTE API #####

##### REQUIREMENTS #####
The project has been developed in Python and is connected to the Fuseki API. Python with libraries pyfuseki, rdflib, numpy, json and flask have to be installed. You also have to install the fuseki-server triplestore manager. 

##### RUN THE PROJECT #####
To run the project, you have to run the flask project and the fuseki server. 

##### RUNNING FLASK SERVER #####
To run the flask server, move to the folder WebApp Flask and run the command line “python app.py” in a python terminal. The server will be running locally, using the port 5000. (http://127.0.0.1:5000)

##### RUNNING FUSEKI SERVER #####
For seek of simplicity and to be able to run update HTTP queries, we have pushed on Github the whole database in the folder Data/tripleStore. You can also find the turtle file that we have used to create this database in the folder Data. 
To run the Apache Fuseki server, you’ll launch the server, allowing update queries on the database folder location using the following command line: 

“fuseki-server - -loc=”YOUR_PATH/semantic_bikes/Data/tripleStore” - - update /database”

Note that YOUR_PATH is the folder where you have pulled the Github repository. Note also that it is very important to use the parameter - - update and the same database name (/database) to be able to run all HTTP queries properly. 
If you are using a Linux OS, we have created a MakeFile which will launch all of these command lines.

