ifndef APP_NAME
	APP_NAME=$(shell basename `pwd`)
endif

.PHONY: build
build:
	@docker build --no-cache -t $(APP_NAME) -f Dockerfile .

.PHONY: ipython
ipython:
	@docker run -it --rm \
		--mount type=bind,src=$(PWD),dst=/usr/src/app \
		advent-of-code \
		ipython

.PHONY: local_shell
local_shell:
	@docker run -it --rm \
		--mount type=bind,src=$(PWD),dst=/usr/src/app \
		advent-of-code \
		/bin/bash

.PHONY: run_day
run_day:
	@docker run -it --rm \
		--mount type=bind,src=$(PWD),dst=/usr/src/app \
		advent-of-code \
		python3 scripts/day$(DAY).py
