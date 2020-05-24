'''
Implement a basic Singly Linked List.

In a singly linked list, we have an ordered list of items as individual Nodes that have pointers to other Nodes.
'''

class SLLNode(object):

	def __init__(self, value):
		self.value = value
		self.next_node = None

#Now we can build out Linked List with the collection of nodes.

a = SLLNode(1)
b = SLLNode(2)
c = SLLNode(3)

a.next_node = b
b.next_node = c

'''
-> a.value
1

-> b.nextnode.value
3
'''