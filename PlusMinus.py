'''
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line.

This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to 10^-4 are acceptable.
'''

def plusMinus(arr):

	if len(arr) == 0:
		return None

	positive = 0
	negative = 0
	zero = 0
	total = len(arr)

	for num in arr:
		if num != 0 and num//abs(num) == 1:
			positive += 1
		elif num != 0 and num//abs(num) == -1:
			negative += 1
		elif num == 0:
			zero += 1

	print('%.6f' % (positive/total))
	print('%.6f' % (negative/total))
	print('%.6f' % (zero/total))

'''
Input:
6
-4 3 -9 0 4 1

Output:
0.500000
0.333333
0.166667
'''
