build:
	sudo docker-compose build

up-d:
	sudo docker-compose up -d

run:
	sudo docker-compose up

stop:
	sudo docker-compose down

make_migrations:
	sudo docker-compose run bot alembic revision --autogenerate -m "added/updated some table"

migrate:
	sudo docker-compose run bot alembic upgrade head

restart:
	sudo docker-compose down
	sudo docker-compose up -d