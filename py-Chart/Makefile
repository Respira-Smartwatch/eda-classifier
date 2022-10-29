PYTHON = $(HOME)/Envs/py-chart/bin/python

##########################################################################
#
#                   SETUP:  INSTALL PYTHON REQUIREMENTS
#					
#
##########################################################################
setup:
	@$(PYTHON) -m pip install -r requirements.txt >/dev/null


respira/bin/activate: requirements.txt
	python3 -m py-chart py-chart
	./py-chart/bin/pip install -r requirements.txt

clean:
	rm -rf ./__pycache__
