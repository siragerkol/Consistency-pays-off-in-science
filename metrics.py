import numpy as np

'''
c: list of citations received for each publication
'''

def E_index(c):
	'''
	function for calculating E-index
	'''
	c = np.array(c)
	N = len(c)
	c = c[c!=0]
	q = c / sum(c)
	E = -sum(c * np.log(q)) / N 

	return(E)


def citation_moment(c, alpha=0.3):
	'''
	function for calculating citation moment (M_alpha)
	alpha: parameter for modulating the weight of citation distribution, should be alpha >= 0
	'''
	c = np.array(c)
	M_alpha = np.mean(c**alpha)

	return(M_alpha)


def h_index(c):
	'''
	function for calculating h-index
	'''
    c = np.array(c)
    paper_ids = np.arange(1, len(c)+1)
    c[::-1].sort()
    H = np.max(np.minimum(c, paper_ids))

    return(H)