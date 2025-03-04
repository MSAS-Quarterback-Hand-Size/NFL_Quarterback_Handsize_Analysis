.PHONY: venv install run clean

# Define Python and Virtual Environment
PYTHON = venv/bin/python
PIP = venv/bin/pip

## Create a virtual environment (forces recreation)
venv:
	rm -rf venv
	python3 -m venv venv

## Install dependencies
install: venv
	$(PIP) install -r requirements.txt

## Run main.py and output to output.txt
run:
	$(PYTHON) main.py > output.txt

## Clean virtual environment and output
clean:
	rm -rf venv output.txt __pycache__

## Show available commands
help:
	@echo "Makefile commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
