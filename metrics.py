import numpy as np

def E_index(c): # c: a list of citations received for each publication
	N = len(c)
	c = np.array(c[c!=0])
	q = c / sum(c)
	E = -sum(c * np.log(q)) / N 
	return (E)


def citation_moment(c, alpha):
	c = np.array(c)
	M_alpha = np.mean(c**alpha)
	return(M_alpha)
