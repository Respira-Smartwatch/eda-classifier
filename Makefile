PYTHON = $(HOME)/Envs/respira/bin/python

##########################################################################
#
#                   SETUP:  INSTALL PYTHON REQUIREMENTS
#					
#
##########################################################################
setup:
	sudo apt update
	sudo apt install -y build-essential python-dev  libopenblas-dev libatlas-base-dev libblas-dev liblapack-dev libsuitesparse-dev python3-pip
	pip3 install -r requirements.txt 


respira/bin/activate: requirements.txt
	python3 -m venv respira
	./respira/bin/pip install -r requirements.txt

clean:
	rm -rf ./src/__pycache__
	rm -rf dataset
