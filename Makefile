start-app:
	docker-compose up --build --force-recreate -d
stop-app:
	docker-compose stop