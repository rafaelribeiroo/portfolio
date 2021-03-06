clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -name "*pyc" -exec rm -rf {} \;i

clearMigrations:
	cd src/apps/dados && rm -rf migrations/	

run:
	python manage.py runserver 127.0.0.1:8000 --settings=src.settings.local

runProduction:
	python manage.py runserver 0.0.0.0:8000 --settings=src.settings.production

migrate:
	python manage.py migrate
	python manage.py dados

migrations:
	python manage.py makemigrations
	python manage.py makemigrations dados

user:
	python manage.py createsuperuser

test:
	python manage.py test

shell:
	python manage.py shell

collect:
	python manage.py collectstatic
