# Local environment

lint-local:
	pre-commit run -va

lint-update-local:
	pre-commit autoupdate

install-requirements-local:
	pip install -r requirements/local.txt
