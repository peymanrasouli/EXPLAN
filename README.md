# EXPLAN

This repository contains implementation codes of the following paper:

EXPLAN: Explaining Black-box Classifiers using Adaptive Neighborhood Generation

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
6- It requires repositories as [content root](https://git-scm.com/book/en/v2/Git-Tools-Submodules). This can be done manually in [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-content-roots.html) or by setting the [PYTHONPATH](https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html).


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




