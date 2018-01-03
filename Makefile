clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -name "*pyc" -exec rm -rf {} \;i

run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

user:
	python manage.py createsuperuser

test:
	python manage.py test

shell:
	python manage.py shell

collect:
	python manage.py collectstatic
