class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def print_linkedlist(self):
		if self.head is None:
			print("no data")
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
		print('pushed',cur.data)

	def merge(self,llist1):

		p=self.head
		q=llist1.head
		s=None
		if not p:
			return q
		if not q:
			return p

		if p.data<q.data:
			s=p
			p=s.next
		if p.data>q.data:
			s=q
			q=s.next

		new_head=s
		while p and q:
			if p.data<=q.data:
				s.next = p 
				s = p 
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next
		if not p:
			s.next=q
		if not q:
			s.next=p
		return new_head

llist=LinkedList()
llist.append("2")
llist.append("1")
llist.append("4")
llist.append("6")
llist1=LinkedList()
llist1.append("3")
llist1.append("8")
llist1.append("5")
llist1.append("7")
llist.merge(llist1)
print(llist.print_linkedlist())

