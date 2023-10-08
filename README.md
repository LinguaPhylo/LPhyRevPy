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

## Example

Rev tutorial https://revbayes.github.io/tutorials/coalescent/constant

LPhy:

```
data {
  D = readFasta(file="data/horses_isochronous_sequences.fasta");
  taxa = D.taxa();
  L = D.nchar();
}
model {
  Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);
  ψ ~ Coalescent(theta=Θ, taxa=taxa);
  π ~ Dirichlet(conc=[1.0,1.0,1.0,1.0]);
  rates ~ Dirichlet(conc=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]);
  Q=gtr(freq=π, rates=rates);
  γ ~ LogNormal(meanlog=0.0, sdlog=2.0);
  r ~ DiscretizeGamma(shape=γ, ncat=4, replicates=L);
  clock ~ LogNormal(meanlog=-16.88, sdlog=5.0);
  D ~ PhyloCTMC(tree=ψ, siteRates=r, Q=Q, mu=clock);
}
```

Rev:

```
D <- readDiscreteCharacterData("data/horses_isochronous_sequences.fasta")
taxa := D.taxa()
Theta ~ dnLognormal(mean=3.0, sd=1.0)
psi ~ dnCoalescent(theta=Theta, taxa=taxa)
rates ~ dnDirichlet(alpha=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
pi ~ dnDirichlet(alpha=[1.0, 1.0, 1.0, 1.0])
Q := fnGTR(exchangeRates=rates, baseFrequencies=pi)
clock ~ dnLognormal(mean=-16.88, sd=5.0)
gamma ~ dnLognormal(mean=0.0, sd=2.0)
r := fnDiscretizeGamma(shape=gamma, rate=gamma, numCats=4)
D_clamp ~ dnPhyloCTMC(tree=psi, Q=Q, branchRates=clock, siteRates=r)
D_clamp.clamp(D)
```

More [examples](./examples)

## Available conversions

1. Commonly used nucleotide substitution models
2. Constant sized coalescent model
3. IID
4. Read sequences
5. Create taxa
6. Basic PhyloCTMC

## TODO

1. Rev Moves
2. Vector match
3. Discrete phylogeography
4. Structured coalescent
5. Birth death models
6. https://revbayes.github.io/tutorials/coalescent/
7. https://revbayes.github.io/tutorials/coalescent/skyline
8. Individual TODOs inside some Python classes

