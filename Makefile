install:
	@echo "Installing dependencies"
	@pip install -r requirements.txt

# create start for starting the web, use env PORT for port
PORT ?= 5000

start:
	@echo "Starting the web"
	@FLASK_APP=main.py .venv/bin/python -m flask run -p $(PORT)

start-dev:
	@echo "Starting the web"
	@FLASK_APP=main.py FLASK_ENV=development FLASK_DEBUG=1 .venv/bin/python -m flask run -p $(PORT)

WEB_TEST_DIR = "Forum API Test"

test:
	@echo "Running tests"
	@newman run $(WEB_TEST_DIR)'/Forum API V1 Test.postman_collection.json' -e $(WEB_TEST_DIR)'/Forum API V1 Test.postman_environment.json' --env-var port=$(PORT) --bail

migrate-up:
	@echo "Migrating up"
	@alembic upgrade head

migrate-down:
	@echo "Migrating down"
	@alembic downgrade base

migrate-rollback:
	@echo "Migrating rollback"
	@alembic downgrade -1

migrate-revision:
	@echo "Migrating revision"
	@alembic revision -m "$(message)"

feature:
	@echo "Creating feature folder"
	@mkdir -p app/$(name)
	@touch app/$(name)/__init__.py
	@touch app/$(name)/entities.py
	@touch app/$(name)/use_cases.py
	@touch app/$(name)/handlers.py
	@touch app/$(name)/routes.py
	@touch app/$(name)/repository.py