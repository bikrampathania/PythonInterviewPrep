'''
Given the Stack class below, implement a Queue class using two stacks!
Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.

Check:

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())

Output:
0
1
2
3
4
'''

class Queue2Stacks(object):

	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self, element):
		self.instack.append(element)

	def dequeue(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())

		return self.outstack.pop()

