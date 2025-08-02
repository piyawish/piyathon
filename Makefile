default:
	@echo "No default task defined"

test:
	find ../cpython -name "*.py" ! -path "*/test/tokenizedata/*" > tests/cpython_file_list.txt
	uv run pytest tests -v -s
	@rm tests/cpython_file_list.txt
	@rm -rf tests/translated

build:
	uv build

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
	uv run twine check dist/*
	uv run twine upload dist/*

test-upload: clean build
	uv run twine check dist/*
	uv run twine upload --repository testpypi dist/*
