import math

import numpy as np

x = np.array([5.0, 5.0, 5.0])

def potential(r):
	R = np.linalg.norm(r)
	return 1 / abs(r)

	print("OK, here we are")
