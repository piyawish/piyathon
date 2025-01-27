default:
	@echo "No default task defined"

test:
	find ../cpython -name "*.py" > tests/cpython_file_list.txt
	pytest tests
	@rm tests/cpython_file_list.txt
	@rm -rf tests/translated

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
