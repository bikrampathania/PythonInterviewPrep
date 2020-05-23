'''
1. Given an integer array, output all the * *unique** pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return "2" pairs

2. FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS:

(1,3)
(2,2)
'''

######################
#                    #
#     Solution 1     #            
#                    #
######################

def pair_sum(arr, k):

	counter = 0
	lookup = set()

	for num in arr:
		if (k - num) in lookup:
			counter += 1
		else:
			lookup.add(num)

	return counter

######################
#                    #
#     Solution 2     #            
#                    #
######################


def pair_sum(arr, k):

	if len(arr) < 2:
		return False

	seen = set()
	output = set()

	for num in arr:

		target = k - num

		if target not in seen:
			seen.add(num)
		else:
			output.add((min(num, target), max(num, target)))

	#return len(output) # to check pair count
	print('\n'.join(map(str, list(output))))











