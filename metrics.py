import numpy as np

'''
c: list of citations for each publication
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
    ids = np.arange(1, c.shape[0] + 1)
    c[::-1].sort()
    H = np.max(np.minimum(c, ids))

    return(H)


def g_index(c):
	'''
	function for calculating g-index
	'''
    c=np.array(c)
    c[::-1].sort()
    c=np.cumsum(c)
    for i in range(len(c)):
        if c[i] < i**2:
            return(i)
    return(i+1)


def q_index(c, mu=0):
	'''
	function for calculating q-index
	mu: a parameter to modulate the range of q-index values
	'''
    c = np.array(c)
    c = c[c!=0]
    Q = np.exp(np.mean(np.log(c)) - mu)
    return(Q)
