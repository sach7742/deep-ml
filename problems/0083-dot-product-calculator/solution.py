import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# a =[1,2,3] , b= =[4,5,6]
	#calculate dot calculate
	# 1) multiply - 1*4, 2*5, 3*6
	# 2) add 4 + 10 +18

	n = len(vec1)
	dot_product = 0
	# n = 3
	for i in range(n):
		dot_product += vec1[i]*vec2[i]
	return dot_product