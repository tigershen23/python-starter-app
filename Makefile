.PHONY: mypy ruff check_ruff fix dev_install lock test snapshot test_live_completion pr fly migrate create_migration reset_db reset_redis graphql benchmarks check_imports version upgrade_version version_commit test_build_and_publish download_and_install build_exponent publish_exponent
mypy:
	mypy --check .

ruff:
	ruff format .
	ruff check --fix .

check_ruff:
	ruff check .

fix:
	make ruff

dev_install:
	pip install poetry
	poetry install --no-root
	pre-commit install --install-hooks
	[ -e python_modules/exponent_server/.env ] || cp python_modules/exponent_server/.env.example python_modules/exponent_server/.env

lock:
	poetry lock

run:
	poetry run myapplication

test:
	poetry run pytest
