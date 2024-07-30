update_pip:
	rm requirements.txt
	pip-compile -v requirements.in
	pip-sync

gen_grammar:
	antlr4 -Dlanguage=Python3 -visitor -listener -o src/piyathon/grammar/generated/ -Xexact-output-dir src/piyathon/grammar/PiyathonLexer.g4
	antlr4 -Dlanguage=Python3 -visitor -listener -o src/piyathon/grammar/generated/ -Xexact-output-dir src/piyathon/grammar/PiyathonParser.g4