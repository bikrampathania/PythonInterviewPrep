'''
Alice and Bob each created one problem for HackerRank.
A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

Given a and b, determine their respective comparison points.

For example, a = [1,2,3] and b = [3,2,1]. For elements 0, Bob is awarded a point because a[0] < b[0].
For the equal elements a[1] and b[1], no points are earned.
Finally, for elements 2, a[2] > b[2] so Alice receives a point.
Your return array would be [1,1] with Alice's score first and Bob's second.
'''

def compareTriplets(a, b):

	alice = 0
	bob = 0

	for i in range(len(a)):
		if a[i] == b[i]:
			continue
		if a[i] > b[i]:
			alice += 1
		else:
			bob += 1

	return [alice, bob]