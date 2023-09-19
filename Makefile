install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=src --cov=src/lib tests/test_*.py
	python -m pytest --nbval src/*.ipynb

format:	
	black src/lib/*.py src/*.py tests/*.py

lint:
	ruff check src/lib/*.py src/*.py

run:
	python3 -m src/main.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy