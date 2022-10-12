# Consistency pays off in science

This is a repository to accompany the paper 'Consistency pays off in science' by Şirag Erkol, Satyaki Sikdar, Filippo Radicchi, and Santo Fortunato.

## Citation Moment and E-index

We propose two measures for identifying excellence in science:
- Citation moment $\left(M_\alpha\right)$
- E-index


### Citation Moment $\left(M_\alpha\right)$

A parametric measure that can potentially reward different types of publication portfolios $\mathcal P$ depending on the value of the parameter $\alpha$.

$$M_\alpha\left(\mathcal P\right) = \frac{1}{N} \sum_{i=1}^N c_i^{\alpha}$$


### E-index

A parameter-free measure sensitive to the distribution of citations, favoring citations distributed equally among papers.

$$E\left(\mathcal P\right) = -\frac{1}{N} \sum_{i=1}^N c_i log\frac{c_i}{C_{tot}}$$

This measure is the product of average citations $\left(C_{avg}\right)$ and Shannon entropy of the citation distribution.

## Other measures

The repository includes functions for calculating some other measures, such as H-index [Hirsch](https://www.pnas.org/doi/abs/10.1073/pnas.0507655102), G-index [Egghe](https://link.springer.com/article/10.1007/s11192-006-0144-7), and Q-index [(Sinatra et al.)](https://www.science.org/doi/full/10.1126/science.aaf5239).


### Symbols

- $c_i$: citations received by publication $i$
- $\mathcal P$: publication portfolio of a scientist, $\mathcal P = \\{c_1, c_2, ..., c_N \\}$
- $N = |\mathcal P|$
- $C_{tot} = \sum_i c_i$
- $C_{avg} = \frac{C_{tot}}{N}$



