fusekiScript=./launchfuseki.sh
PYTHON=python3
PIP=pip3
REQUIREMENTS=requirements.txt
APPDIR="WebApp Flask"
APPFILE=app.py
STORE=database
HOST=localhost
PORT=3030


.PHONY: all fuseki app install run env

all: run

install:
	$(PIP) install -r requirements.txt

env:
	$(PIP) install pipenv
	pipenv install
	pipenv shell

run: fuseki app

fuseki:
	$(fusekiScript) $(STORE) &
	./wait-for-it.sh "$(HOST):$(PORT)" -- echo "Fuseki is up at $(HOST):$(PORT)/$(STORE)"

app:
	cd $(APPDIR); $(PYTHON) $(APPFILE)

