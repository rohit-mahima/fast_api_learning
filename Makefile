setup_tests:
	pre-commit install
	python3 -m unittest -v
	python3 -m pip install -r requirements.txt
