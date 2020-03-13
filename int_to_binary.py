from programs import *

def int_to_bin(num):
	s=Stack()
	bin=""
	while num>0:
		rem=num%2
		s.push(rem)
		num=num//2

	while not s.is_empty():
		bin+=str(s.pop())
	
	return bin

print(int_to_bin(15))