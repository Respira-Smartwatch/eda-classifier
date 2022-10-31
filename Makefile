PYTHON = $(HOME)/Envs/respira/bin/python

##########################################################################
#
#                   SETUP:  INSTALL PYTHON REQUIREMENTS
#					
#
##########################################################################
setup:
	@$(PYTHON) -m pip install -r requirements.txt >/dev/null

respira/bin/activate: requirements.txt
	python3 -m venv respira
	./respira/bin/pip install -r requirements.txt

clean:
	rm -rf ./src/__pycache__
	rm -rf dataset
