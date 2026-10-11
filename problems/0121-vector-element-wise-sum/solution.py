def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# a=[1,3] , b=[4,5]
	if len(a) != len(b):
		# if 2!= 2 
        return -1
		#does not run 
	n = len(a)
	# n = 2
	sums  = [1] * n 
	# sums = [1,1]
	# a = [1,3] 
	# b = [4,5]
	# s = [1+4,3+5]
	for i in range(n):
		# i = 0,1 
    	sums[i]= [a[i]+b[i]]
		# for i = 0 , a[0] =a[0]+ b[0], = a[0]= 1 + 4 = 5
		# for i = 1 , a[1] = a[1]+ b[1] = a[1] = 3+5 = 8
    return sums

		

	
	 