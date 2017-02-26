class SLLNode(object):
		'''
		Node Class for SingleLinkedList class
		'''
		def __init__(self, data=0):
			'''
			Constructor for Node Class
			'''
			self.__value = data
			self.__next = None

		def getValue(self):
			'''
			Returns the Value of the Node
			'''
			return self.__value

		def setValue(self, data):
			'''
			Sets the Value of the Node
			'''
			self.__value = data

		def getNext(self):
			'''
			Returns the NextPtr of the Node
			'''
			return self.__next

		def setNext(self, node_obj):
			'''
			Sets the NextPtr of the Node
			'''
			self.__next = node_obj


class SingleLinkedList(object):
	'''
	Python 2.7 implementation of Single Linked List
	'''
	def __init__(self):
		'''
		Constructor of SingleLinkedList class
		'''
		self.head = None
		self.tail = None
		self.size = 0

	def length(self):
		'''
		Function returns the size of the LinkedList
		'''
		return self.size

	def addToHead(self, data):
		'''
		Adds new node to the Head of the List
		'''
		if (self.head == None):
			#If there exists no Nodes in the List
			new_node = SLLNode(data)
			self.head = new_node
			self.tail = self.head
			#Increment size of the List
			self.size += 1
		else:
			tmp_node = self.head
			new_node = SLLNode(data)
			new_node.setNext(tmp_node)
			self.head = new_node
			#Increment size of the list
			self.size += 1

	def addToTail(self, data):
		'''
		Adds new node to the Tail of the List
		'''
		if (self.tail == None):
			self.addToHead(data)
		else:
			new_node = SLLNode(data)
			self.tail.setNext(new_node)
			self.tail = new_node
			self.size += 1

	def add(self, data):
		'''
		Adds new Node to the Tail of the List
		'''
		self.addToTail(data)

	def removeFromHead(self):
		if (self.size == 0):
			print "Cannot Remove From Head. List is empty"
		else:
			tmp_node = self.head.getNext()
			print 'Removing From Head: {}'.format(self.head.getValue())
			del(self.head)
			self.head = tmp_node
			#Decrement the size of the List
			self.size -= 1
	
	def removeFromTail(self):
		if(self.size == 0):
			print "Cannot Remove From Head. List is empty"
		else:
			#Travel to the tail
			tmp_node = self.head
			while(tmp_node.getNext() != self.tail):
				tmp_node = tmp_node.getNext()
			#Save the previous node to tail
			print 'Removing from Tail: {}'.format(self.tail.getValue())
			del(self.tail)
			self.tail = tmp_node
			#Decrement the size of the list
			self.size -= 1

	def remove(self):
		self.removeFromTail()

	def printList(self):
		print "Printing Singly Linked List"
		tmp_head = self.head
		if (self.size == 0):
			print "List is empty!"
		else:
			tmp_size = self.size
			while (tmp_size > 0):
				print '{} '.format(tmp_head.getValue()),
				tmp_head = tmp_head.getNext()
				tmp_size -= 1
			print ""

def main():
	'''
	Main funciton to test the class
	'''
	mysll = SingleLinkedList()
	mysll.addToHead(2)
	mysll.addToTail(4)
	mysll.addToTail(9)
	mysll.addToTail(3)
	mysll.addToTail(5)
	mysll.printList()
	mysll.removeFromHead()
	mysll.printList()
	mysll.removeFromTail()
	mysll.printList()

if __name__ == "__main__":
	main()


  
