# Local environment

lint-local:
	pre-commit run -va

lint-update-local:
	pre-commit autoupdate

install-requirements-local:
	pip install -r requirements/local.txt

run-local:
	uvicorn main:app \
		--reload \
		--host=0.0.0.0 \
		--port=9600 \
		--log-level=debug \
		--use-colors

open-api-json-local:
	open http://0.0.0.0:9600/openapi.json
