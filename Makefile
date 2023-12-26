install:
	@echo "Installing dependencies"
	@pip install -r requirements.txt

# create start for starting the web, use env PORT for port
PORT ?= 5000

start:
	@echo "Starting the web"
	@.venv/bin/python -m flask run -p $(PORT)

WEB_TEST_DIR = "Forum API Test"

test:
	@echo "Running tests"
	@newman run $(WEB_TEST_DIR)'/Forum API V1 Test.postman_collection.json' -e $(WEB_TEST_DIR)'/Forum API V1 Test.postman_environment.json' --env-var port=$(PORT) --bail