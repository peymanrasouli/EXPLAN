# EXPLAN

This repository contains implementation codes of the following paper:

EXPLAN: Explaining Black-box Classifiers using Adaptive Neighborhood Generation

# Setup
1- The repository contains [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). When cloning the repository, make sure you clone with submodules:
```
git clone --recurse-submodules https://github.com/peymanras/EXPLAN

```
2- It may require some repositories as [content root](https://git-scm.com/book/en/v2/Git-Tools-Submodules). This can be done manually in [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-content-roots.html) or by setting the [PYTHONPATH](https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html).

3- After cloning, run initial setup:
```
python setup.py
```

4- We recommend using Anaconda Python 3.6 distribution for other required libraries. 

# Reproducing the results
1- To reproduce the fidelity and coverage results run:
```
python fidelity_coverage_experiments.py
```

2- To reproduce the stability results run:
```
python stability_experiments.py
```


