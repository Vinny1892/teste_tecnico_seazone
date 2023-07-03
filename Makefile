SHELL=/bin/bash

.PHONY: help
help:  ## Show the help
	@echo "██████╗ ███████╗ ██████╗ ██╗   ██╗██╗     ██╗   ██╗███████╗"
	@echo "██╔══██╗██╔════╝██╔════╝ ██║   ██║██║     ██║   ██║██╔════╝"
	@echo "██████╔╝█████╗  ██║  ███╗██║   ██║██║     ██║   ██║███████╗"
	@echo "██╔══██╗██╔══╝  ██║   ██║██║   ██║██║     ██║   ██║╚════██║"
	@echo "██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗╚██████╔╝███████║"
	@echo "╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
.PHONY: up

up: ## start application
	@docker-compose up

.PHONY: up-silent
up-silent: ## start application in detach mode
	@docker-compose up -d

.PHONY: test
test:   ## execute all tests application
	@docker-compose exec -T api python manage.py test

.PHONY: shell
shell:  ## running shell inside container
	docker-compose exec api bash

.PHONY: logs
logs:   ## show all logs
	@docker-compose logs -f

.PHONY: psql
psql:   ## connect to postgres database
	@docker-compose exec postgres psql "postgresql://postgres:postgres@postgres/credenciamento_dev"

.PHONY: shell_python
tinker:  ## connect shell in application
	@docker-compose exec api python  manage.py  shell_plus

.PHONY: down
down:  ## stop and kill all services
	@docker-compose down

.PHONY: stop
stop:  ## stop one or all services
	@docker-compose stop ${SERVICE}

.PHONY: restart
restart:  ## restart one or all services
	@docker-compose restart ${SERVICE}

.PHONY: db-seed
db-seed: ## seed database
	@docker-compose exec api  python manage.py create_immobile 5  && \
		python manage.py create_announcement 3  && \
 		python manage.py create_reserve 8

.PHONY: create-immobile
create-immobile: ## create immobile in database
	@docker-compose exec api  python manage.py create_immobile ${NUMBER}

.PHONY: create-announcement
create-announcement: ## create announcement in database
	@docker-compose exec api python manage.py create_announcement ${NUMBER}

.PHONY: create-reserve
create-reserve: ## create reserve in database
	@docker-compose exec api python manage.py create_reserve ${NUMBER}

.PHONY: build-no-cache
build-no-cache: ## build image with any cache
	@docker-compose build --no-cache --pull ${BUILD_ARGS}

.PHONY: docker-development-image
docker-development-image: ## build development image with image name passing in param
	@docker build -f docker/development/dockerfile.dev -t ${IMAGE_NAME} .

.PHONY: docker-production-image
docker-production-image: ## build production image with image name passing in param
	@docker build -f docker/production/dockerfile.prod -t ${IMAGE_NAME} .
