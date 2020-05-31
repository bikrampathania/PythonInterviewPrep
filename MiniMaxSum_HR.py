'''
Given five positive integers, find the minimum and maximum values that can be calculated
by summing exactly four of the five integers.

Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example, arr = [1,3,5,7,9]. Our minimum sum is 1+3+5+7=16 and our maximum sum is 3+5+7+9=24.

We would print: 16 24
'''

def miniMaxSum(arr):

	if len(arr) < 5:
		return False
	
	arr = sorted(arr)

	min = max = 0

	for num in arr[1:5]:
		max += num

	for num in arr[0:4]:
		min += num

	print(min, max)
