#Iterative algorithm so that every fibonacci number is computed exactly once

#Time complexity of the algorithm is thus O(n)


def fib(n):
	current = int
	previous = int
	current = 1
	previous = 0
	nex = int
	for i in range(2,n):
		nex = previous + current 
		previous = current
		current = nex
		print(nex)
fib(10)
