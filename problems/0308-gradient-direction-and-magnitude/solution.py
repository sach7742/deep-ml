import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	#magnitude : sqrt(sum(x^2))

	#gradient = [3.0, 4.0]
	#step 0 : do step 1 to 3 till all list is exhausted 
	#step 1 : pick a  number in the vector 
	#step 2: square the pickked number 
	# step 3 : store the squared number in a list 
	# step 4 : sum the number in list 
	# step 5: sqrt the sum of number

    n = len(gradient)
    squares = []
	for i in range(n):
		a= (gradient[i])**2
		squares.append(a)
	
	magnitude = sum(squares)**0.5
	
	output = {
		"magnitude" : 2.0,
		"direction": 3.1,
		"descent_direction":2.1 
	}
    output["magnitude"]= magnitude
	

	# steps for direction 
	#step 0 : do step 1 to 2 till all list is exhausted 
	# step 1: pick a number in vector 
	# step 2: divide it by magnitude 
	# step 3 : store direction

	n = len(gradient)
    directions = []
	for i in range(n):
		if(magnitude==0.0):
			direction=gradient[i]
		else:
			direction= (gradient[i])/magnitude
		directions.append(direction)
	output["direction"] = directions

	# descent direction 
	# step1: choose a number from list direction
	# step 2: multiply that num by -1
	# step 3: store those numbers in list 

    n = len(directions)
	descent_direction =[]
	for i in range(n):
		descent = directions[i]*(-1)
		descent_direction.append(descent)
	output["descent_direction"]=descent_direction

	return output







	










