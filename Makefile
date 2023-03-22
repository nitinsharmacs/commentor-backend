run-test:
	PYTHONPATH=. pytest -v $(args)

print:
	echo $(args)

start:
	python3 main.py