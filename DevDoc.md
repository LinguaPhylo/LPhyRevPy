# Developer Documentation

The parser is created using ANTLR grammar, 
which is exported from [LPhy project](https://github.com/LinguaPhylo/linguaPhylo).
The Python classes matching with LPhy Java classes are implemented to convert LPhy language into Rev language.
The `RevBuilder` class will collect the objects parsed by parser 
and call `lphy_to_rev` method in each python class to print the Rev code accordingly.
Those classes are still kept the simplified class structure, 
including the concept of `Generator`, `Value`, `Function`, and `GenerativeDistribution`.

## Python class

The class name (e.g. GenerativeDistribution) will be used to match with the LPhy language,
which is case-sensitive. 
But for any class name cannot be matched with the LPhy language during the implementation,
especially all function names, the attribute `generator_info` can be used to define the name.
Please see `JukesCantor.py` under `lphy.base.evolution.substitutionmdoel` as an example.

Since the simulated value is not considered as the feature at this stage,
all methods `sample` or `apply` can return a `RandomVariable` or `Value` containing `None` as its value,
except that some special classes, such as `Taxa` under `lph.base.evolution.taxa`.

## Argument names

The Python class only creates one `__init__`, where all arguments names must match with 
the corresponding LPhy function or distribution's arguments, except of `self`.
Their types must be the `Value` object.
The optional arguments must have a default value of `None`.

If arguments are unnamed, then it has to be `arg_` plus an integer index starting from 0,
such as `arg_0` in the class `Length` under `lphy.base.function`.

## LPhy data type

Taking advantage of Python's dynamic typing, the `Value` object 
does not handle the data types anymore. The same is parsing.

## LPhy array

All LPhy arrays will convert to the Python list, and map will convert to the dictionary.
The type checking can be done by `if not isinstance(theta_val, list)`.

## Vectorization vs. for loop

### IID

The IID will be converted into `for` loop in the class `IID` under `lphy.core.vectorization`.

During the conversion, the assignment has to be inside the loop,
so the corresponding class (e.g. Taxa) must overwrite the method `has_var_declaration_rev` to return _False_ as below:

```python
def has_var_declaration_rev(self):
   return False
```

## Different implementations between LPhy and Rev

### 1. Taxa

Use the flag to create a `for` loop to create taxa vector in Rev.

### 2. Nexus file

Rev does not fully support Nexus format, such as codons, and Nucleotide data type. 
Only "DNA" keyword is recognised in the data type. 

LPhy provides `options` to define optional arguments for reading data. 
For example, it can be an option to extract the sample times from the taxa labels using a regular expression, 
or an option to treat those times as dates (forward) or ages (backward).
In the alignment, the method `.charset()` can be used to split it into multiple partitions, 
such as 3 alignments for codons.

It seems Rev has to load the dates/ages from a separated file, and also splitting alignment is not available. 

### 3. DiscretizeGamma and PhyloCTMC

LPhy implements differently in `PhyloCTMC`, where the LPhy `siteRates` are the rate for each site in the alignment. 
The `DiscretizeGamma` handles the approximation inside. 
The LPhy code `r ~ DiscretizeGamma(shape=γ, ncat=4, replicates=L)` will return the vector of site rates by IID, 
where each rate is randomly picked up from 4 rates drawn from a Gamma distribution. 
The vector length equals to the number of sites. 

However, the `siteRates` with the same name in Rev `dnPhyloCTMC` takes the rate categories, 
which is a vector returned by `fnDiscretizeGamma`, but its length equals to the number of categories,
such as 4.

### 4. Skyline model prior

Rev uses the `for` loop to implement the Skyline model prior.
For example, for the Bayesian Skyline Plot (Drummond et al. 2005),
The LPhy prior `ExpMarkovChain` is equivalent to a Rev `for` loop, 
which makes the population sizes in neighbouring intervals correlated.

