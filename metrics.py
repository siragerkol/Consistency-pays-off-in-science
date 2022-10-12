import numpy as np

def E_index(c):
	'''
	function for calculating E-index
	c: list of citations received for each publication
	'''
	c = np.array(c)
	N = len(c)
	c = c[c!=0]
	q = c / sum(c)
	E = -sum(c * np.log(q)) / N 
	return (E)


def citation_moment(c, alpha=0.3):
	'''
	function for calculating citation moment (M_alpha)
	c: list of citations received for each publication
	alpha: parameter for modulating the weight of citation distribution, should be alpha >= 0
	'''
	c = np.array(c)
	M_alpha = np.mean(c**alpha)
	return(M_alpha)

