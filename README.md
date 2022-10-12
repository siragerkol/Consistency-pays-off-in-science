# Consistency pays off in science

This is a repository to accompany the paper 'Consistency pays off in science' by Şirag Erkol, Satyaki Sikdar, Filippo Radicchi, and Santo Fortunato.


## Citation Moment and E-index

We propose two measures for identifying excellence in science:
- Citation moment $\left(M_\alpha\right)$
- E-index


### Citation moment $\left(M_\alpha\right)$

A parametric measure that can potentially reward different types of publication portfolios $\mathcal P$ depending on the value of the parameter $\alpha$.

$$M_\alpha\left(\mathcal P\right) = \frac{1}{N} \sum_{i=1}^N c_i^{\alpha}$$


### E-index

A parameter-free measure sensitive to the distribution of citations, favoring citations distributed equally among papers.

$$E\left(\mathcal P\right) = -\frac{1}{N} \sum_{i=1}^N c_i log\frac{c_i}{C_{tot}}$$

This measure is the product of average citations $\left(C_{avg}\right)$ and Shannon entropy of the citation distribution $\sum_{i}^{N}$.


### Symbols

- $c_i$: citations received by publication $i$
- $\mathcal P$: publication portfolio of a scientist, $\mathcal P = \\{c_1, c_2, ..., c_N \\}$
- $N = |\mathcal P|$
- $$\sum_i^N$$


$C_{tot} = \sum_{i=1}^N c_i$
