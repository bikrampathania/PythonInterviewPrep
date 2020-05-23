'''
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:

5 is the missing number
'''

######################
#                    #
#     Solution 1     #            
#                    #
######################

def finder(arr1, arr2):

	if len(arr1) == len(arr2):
	    return False

	arr1.sort()
	arr2.sort()

	for num1, num2 in zip(arr1, arr2):
		if num1 != num 2:
			return num1

	return arr1[:-1]

######################
#                    #
#     Solution 2     #            
#                    #
######################

import collections

def finder(arr1, arr2):

	d = collections.defaultdict(int)

	for num in arr2:
		d[num] += 1

	for num in arr1:
		if d[num] == 0:
			return num
		else:
			d[num] -= 1
