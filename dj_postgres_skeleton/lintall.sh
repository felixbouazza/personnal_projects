docker-compose exec -T dj-postgres-back isort .
docker-compose exec -T dj-postgres-back flake8 .
docker-compose exec -T dj-postgres-back black .

sudo chown -R $USER:$USER .