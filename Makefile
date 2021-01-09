isort:
	isort .

black:
	black .

lint: isort black

clean:
	find . -name '*.pyc' | xargs rm -rf
	find . -name '*__pycache__' | xargs rm -rf
	find . -name '*.cache' | xargs rm -rf

requirements:
	poetry export -f requirements.txt --output requirements.txt

dev_requirements:
	poetry export -f requirements.txt --output requirements.txt --dev

run:
	DEBUG=True ./manage.py runserver
