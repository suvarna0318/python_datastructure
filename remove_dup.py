class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def print_linkedlist(self):

		if self.head is None:
			return
		cur=self.head
		while cur:
			print(cur.data)
			cur=cur.next

	def append(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
			return
		cur=self.head
		while cur.next:
			cur=cur.next	
		cur.next=new_node
		

	def remove_duplicates(self):
		
		d={}
		cur=self.head
		pre=None
		while cur:
			# print("1")
			if cur.data in d:
				pre.next=cur.next
				cur=None
				# print("2")
			else:
				d[cur.data]=1
				pre=cur
				# print("3")
			cur=pre.next

llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("A")
llist.append("D")
llist.append("C")
print(llist.print_linkedlist())
print("remove remove_duplicates")
print(llist.remove_duplicates())
print(llist.print_linkedlist())




