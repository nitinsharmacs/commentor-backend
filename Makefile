run-test:
	PYTHONPATH=. pytest -v $(args)

print:
	echo $(args)