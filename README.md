# EXPLAN

This repository contains the implementation source code of the following paper:

P. Rasouli and I. C. Yu, ["EXPLAN: Explaining Black-box Classifiers using Adaptive Neighborhood Generation,"](https://ieeexplore.ieee.org/document/9206710) 2020 International Joint Conference on Neural Networks (IJCNN), Glasgow, United Kingdom, 2020, pp. 1-9, doi: 10.1109/IJCNN48605.2020.9206710.

# Setup
1- Clone the repository using HTTP/SSH:
```
git clone https://github.com/peymanrasouli/EXPLAN
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
