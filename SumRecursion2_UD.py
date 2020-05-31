'''
Given an integer, create a function which returns the sum of all the individual digits in that integer.
For example: if n = 4321, return 4+3+2+1
'''

def recSum2(n):
	if n == 0:
		return 0 # base case
	else:
		return n%10 + recSum2(n//10) # recursive case
