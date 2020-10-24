.PHONY: down build up reset tests run pull

export TAG_TGFR=$(shell git describe --always --tags --dirty)

run:
	docker rm -f tgfr-qar || echo ""
	docker run -dit --name tgfr-qar -p 9000:9000 tgfr-qar:${TAG_TGFR}
	docker ps

pull:
	git pull

tests: build
	docker run -it --rm --name tgfr-qar-tests tgfr-qar:${TAG_TGFR} bash -c "python -m pytest -vv ."

reset: down build up

down:
	docker-compose down

up:
	docker-compose up -d

build:
	docker-compose build --parallel
