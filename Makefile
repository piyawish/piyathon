update_pip:
	rm requirements.txt
	pip-compile -v requirements.in
	pip-sync

test:
	pytest tests

list_python_files:
	find ../cpython -name "*.py" > tests/cpython_file_list.txt