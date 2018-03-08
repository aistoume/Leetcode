### Youbin 2017/07/27
### 382 Linked List Random Node

from time import time
from random import randint
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def __init__(self, head):
		curr = head
		global n,h
		n = 1
		while curr.next!=None:
			n+=1
			curr = curr.next
		h = head
	def getRandom(self):
		r = randint(1,n)
		curr = h
		while r>1:
			curr = curr.next
			r-=1
		return curr.val
		
        


l = range(5)
h = ListNode(l[0])
curr = h
for i in l[1:len(l)]:
	curr.next = ListNode(i)
	curr = curr.next
	
s = Solution(h)
r = s.getRandom()
print r