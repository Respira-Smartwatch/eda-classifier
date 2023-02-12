# Author: Matteo Vidali, Joseph Bellahcen

setup:
	sudo apt update
	sudo apt install -y libopenblas-dev libatlas-base-dev libblas-dev liblapack-dev libsuitesparse-dev
	CPPFLAGS="-I/usr/include/suitesparse" pip3 install -r requirements.txt 

.PHONY: setup

clean:
	rm -rf ./src/__pycache__
	rm -rf dataset

.PHONY: clean

