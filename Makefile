update_pip:
	rm requirements.txt
	pip-compile -v requirements.in
	pip-sync

test:
	find ../cpython -name "*.py" > tests/cpython_file_list.txt
	pytest tests
