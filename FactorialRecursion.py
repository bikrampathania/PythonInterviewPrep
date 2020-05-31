'''
Write a program to calculate factorial of a number n.
'''

def factorial(n):

	if n == 0: 
		return 1 # Base case
	else:
		return n * factorial(n-1) # recursive case

'''
print(factorial(5))

120
'''