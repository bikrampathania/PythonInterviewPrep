'''
Your function will accept a number n and return the nth number of the fibonacci sequence.

Do it recursively, iteratively and Dynamically

Input: fibonacciRecur(10)
Output: 55
'''

# Recursively

def fibonacciRec(n):

	if n == 0 or n == 1:
		return n
	else:
		return fibonacciRec(n - 1) + fibonacciRec(n - 2)

# Iteratively

def fibonacciIter(n):

	 a, b = 0, 1

	 for i in range(n):

	 	a, b = b, a + b

	 return a

# Dynamically

n = 10
cache = [None] * (n + 1)

def fibonacciDyn(n):

    # Base case
	if n == 0 or n == 1:
		return n

	# Check cache
	if cache[n] != None:
		return cache[n]

	# Keep setting cache
	cache[n] = fibonacciDyn(n - 1) + fibonacciDyn(n - 2)

	return cache[n]
