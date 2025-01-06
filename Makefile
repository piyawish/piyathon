default:
	@echo "No default task defined"

update_pip:
	-rm requirements.txt
	pip-compile -v requirements.in
	pip-sync

test:
	find ../cpython -name "*.py" > tests/cpython_file_list.txt
	pytest tests

build:
	hatch build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type f -name ".pytest_cache" -delete

upload: clean build
	twine check dist/*
	twine upload dist/*

test-upload: clean build
	twine check dist/*
	twine upload --repository testpypi dist/*
