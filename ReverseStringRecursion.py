'''
Reverse a string using recursion. Make sure to think of the base case here.

Input: reverse('hello world')
Output: 'dlrow olleh'
'''

def reverse(s):

	# Base case
	if len(s) <= 1:
		return s

	# Recursive case
	return reverse(s[1:]) + s[0]