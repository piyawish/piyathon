update_pip:
	rm requirements.txt
	pip-compile -v requirements.in
	pip-sync

c2p:
	code2prompt . -o c2p.md --tokens
	code2prompt src -o c2p-src.md --tokens
	code2prompt utils -o c2p-utils.md --tokens
	code2prompt tests -o c2p-tests.md --tokens