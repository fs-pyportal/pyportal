.DEFAULT_GOAL := help
.PHONY: all


DEV_COMPOSE = "./docker-compose.dev.yml"

start-dev:      ## Start development servers with docker compose
	docker compose -f ${DEV_COMPOSE} up -d
stop-dev:       ## Stop development servers
	docker compose -f ${DEV_COMPOSE} down
destroy-dev:    ## Clean development containers, images and volumes
	docker compose -f ${DEV_COMPOSE} down -v --remove-orphans
docker-dev:     ## Run docker commands for development environment, 
                ## ex. "make docker-dev -- logs -f minio"
	docker compose -f ${DEV_COMPOSE} $(-*-command-variables-*-) $(filter-out $@,$(MAKECMDGOALS))

help:
	@echo "Usage:\n  make [target]"
	@echo "Targets: \n"
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)
