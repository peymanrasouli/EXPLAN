# EXPLAN

This repository contains implementation codes of the following paper:

Peyman Rasouli and Ingrid Chieh Yu, "EXPLAN: Explaining Black-box Classifiers using Adaptive Neighborhood Generation", In Proceedings of The International Joint Conference on Neural Networks (IJCNN), Glasgow, 2020.

# Setup
1- Clone the repository using HTTP/SSH:
```
git clone https://github.com/peymanras/EXPLAN
```
2- Create a conda virtual environment:
```
conda create -n EXPLAN python=3.6
```
3- Activate the conda environment: 
```
conda activate EXPLAN
```
4- Standing in EXPLAN directory, install the requirements:
```
pip install -r requirements.txt
```
5- Run initial setup:
```
python setup.py
```
6- Install TBB library required by YaDT:
```
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install libtbb2 

# CentOS
sudo yum update
sudo yum install tbb
```

# Reproducing the results
1- To test EXPLAN on a single instance run:
```
python test_explan.py
```
2- To reproduce the fidelity and coverage results run:
```
python fidelity_coverage_experiments.py
```
3- To reproduce the stability results run:
```
python stability_experiments.py
```
