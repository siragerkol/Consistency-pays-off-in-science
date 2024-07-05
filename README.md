# Consistency pays off in science

This repository contains the code for *Consistency pays off in science* (2023), Ş. Erkol, S. Sikdar, F. Radicchi, and S. Fortunato. Quantitative Science Studies.
- [Paper](https://direct.mit.edu/qss/article/4/2/491/115369/Consistency-pays-off-in-science)
- [arXiv preprint](https://arxiv.org/abs/2210.08440)
- [Website](https://e-index.net/)

## Classification

The notebook [`classification.ipynb`](https://github.com/siragerkol/Consistency-pays-off-in-science/blob/main/classification.ipynb) can be used to replicate the full portfolio classification results for Chemistry.

## Citation Moment and E-index

We propose two measures for identifying excellence in science:
- Citation moment $\left(M_\alpha\right)$
- E-index


### Citation Moment $\left(M_\alpha\right)$

A parametric measure that can potentially reward different types of publication portfolios $\mathcal P$ depending on the value of the parameter $\alpha$.

$$M_\alpha\left(\mathcal P\right) = \frac{1}{N} \sum_{i=1}^N c_i^{\alpha}$$


### E-index

A parameter-free measure sensitive to the distribution of citations, favoring portfolios with citations distributed equally among papers.

$$E\left(\mathcal P\right) = -\frac{1}{N} \sum_{i=1}^N c_i log\frac{c_i}{C_{tot}}$$

This measure is the product of average citations $\left(C_{avg}\right)$ and Shannon entropy of the citation distribution.


### Symbols

- $c_i$: citations received by publication $i$
- $\mathcal P$: publication portfolio of a scientist, $\mathcal P = \\{c_1, c_2, ..., c_N \\}$
- $N = |\mathcal P|$
- $C_{tot} = \sum_i c_i$
- $C_{avg} = \frac{C_{tot}}{N}$



## Other measures

The repository includes functions for calculating some other measures, such as H-index [(Hirsch)](https://www.pnas.org/doi/abs/10.1073/pnas.0507655102), G-index [(Egghe)](https://link.springer.com/article/10.1007/s11192-006-0144-7), and Q-index [(Sinatra et al.)](https://www.science.org/doi/full/10.1126/science.aaf5239).


## E-index portal

We have created the portal [e-index.net](https://e-index.net/)! You can use the website to search for [scientists](https://e-index.net/author) and see their citation measures, including E-index. You can [compare](https://e-index.net/compare) the measures of two different scientists, and see how they rank in their field. You can also check the [hall of fame](https://e-index.net/openalex/hof/) in each field for various citation measures. We use [OpenAlex](https://docs.openalex.org/) API to fetch the portfolios of scientists. 
