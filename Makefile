update_pip:
	rm requirements.txt
	pip-compile -v requirements.in
	pip-sync

test:
	pytest tests