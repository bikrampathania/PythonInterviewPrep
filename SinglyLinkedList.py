'''
Implement a basic Singly Linked List.

In a singly linked list, we have an ordered list of items as individual Nodes that have pointers to other Nodes.
'''

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

#Now we can build out Linked List with the collection of nodes.

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

'''
-> a.value
1

-> b.nextnode.value
3
'''