.PHONY: ruff check_ruff fix dev_install test run docker_run

typecheck:
	pyright

ruff:
	ruff format .
	ruff check --fix .

check_ruff:
	ruff check .

fix:
	make ruff
	make typecheck

dev_install:
	pip install poetry
	poetry install --no-root
	pre-commit install --install-hooks

run:
	poetry run myapplication

docker_run:
	docker build -t myapplication .
	docker run --env-file .env myapplication

test:
	poetry run pytest
