class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LL:
	def __init__(self):
		self.head = None

	def insert_at_end(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = new_node

	def insert_at_begin(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_at_index(self,index,data):
		if index == 0:
			self.insert_at_begin(data)
			return

		curr = self.head
		prev = None
		new_node = Node(data)
		idx = 0
		while curr:
			if idx == index:
				new_node.next = prev.next
				prev.next = new_node
				return
			prev = curr
			curr = curr.next
			idx += 1

		#insert at end
		self.insert_at_end(data)

	def remove_head(self):
		if self.head is None:
			return None
		self.head = self.head.next

	def remove_tail(self):
		if self.head is None:
			return None
		
		if self.head.next is None:
			self.head = None
			return None

		curr = self.head
		while curr.next.next is not None:
			curr = curr.next

		curr.next = None

	def remove_at_index(self,index):
		# no linked list
		if self.head is None:
			return None

		# index = 0 (remove head)
		if index == 0:
			self.remove_head()
			return
		idx = 0
		prev = None
		curr = self.head
		while curr:
			if idx == index:
				prev.next = curr.next
				return
			
			prev = curr
			curr = curr.next
			idx += 1

	def remove_node(self,data):
		# no linkedlist
		if self.head is None:
			return None
		curr = self.head
		prev = None

		# if first node is data
		if self.head.data == data:
			self.remove_head()
			return

		while curr:
			if curr.data == data:
				prev.next = curr.next
				return
			prev = curr
			curr = curr.next
				

	def traverse(self):
		curr = self.head
		while curr:
			print(curr.data, end='->')
			curr = curr.next
		print('None')

	def size_of_ll(self):
		size = 0
		curr = self.head
		while curr:
			size += 1
			curr = curr.next
		return size

ll = LL()

ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_index(4,100)
# ll.insert_at_index(3,101)
# ll.insert_at_end(1)
# ll.insert_at_end(2)
# ll.insert_at_end(3)
# ll.insert_at_end(4)
# ll.insert_at_end(5)
# ll.remove_head()
# ll.remove_tail()
# ll.remove_tail()
# ll.remove_tail()
# ll.remove_tail()
# ll.remove_head()
# ll.remove_at_index(4)
# ll.remove_node(4)
# ll.remove_node(2)
# ll.remove_node(1)
# ll.remove_node(5)
ll.traverse()
print(ll.size_of_ll())