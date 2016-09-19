class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

	

class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None


	def PrintAllVals(self):
		runner = self.head
		while (runner.next != None):
			print(runner.value)
			runner = runner.next
		else:
			print (runner.value)

	def AddBack(self, value):
		self.tail.next = value




list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
list.head.next.next.next = Node('Eric')
list.head.next.next.next.next = Node('Fred')


list.AddBack(Node('George'))


AddBack(val)
AddFront(val)
InsertBefore(nextVal, val)
InsertAfter(preval, val)
RemoveNode(val)
ReverseList()