'''
Given an array of integers (positive and negative) find the largest continuous sum.

-> large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
29 
'''

def large_cont_sum(arr):

	if len(arr) == 0:
		return 0

	current_sum = max_sum = arr[0]

	for num in arr[1:]:

		current_sum = max(current+sum + num, num)

		max_sum = max(max_sum, current_sum)

	return max_sum