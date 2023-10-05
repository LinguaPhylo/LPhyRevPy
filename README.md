# LPhyRevPy
Convert LPhy models to RevBayes script.

## Usage

Python 3.9 or higher

This project is currently in development. 
Please check out the source code to run __init__.py under the project root.
Prefer to run using IDE, such as PyCharm.

Usage:
```antlrv4
__init__.py -i <inputfile> -o <outputfile>
```

## Available conversions

1. Commonly used nucleotide substitution models
2. Constant sized coalescent model
3. IID
4. Read sequences
5. Create taxa
6. Basic PhyloCTMC

See also [examples](./examples)

## TODO

1. Vector match
2. LPhy method call in TimeTree
3. Discrete phylogeography
4. Structured coalescent
5. Birth death models
6. https://revbayes.github.io/tutorials/coalescent/
7. https://revbayes.github.io/tutorials/coalescent/skyline
8. Individual TODOs inside some Python classes

