# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 09:50:01 2016

@author: Youbin
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		r = None
		n = 0
		while l1 or l2:
			if l1:
				n+=l1.val
				l1= l1.next
			if l2:
				n+=l2.val
				l2= l2.next
			if not r:
				r = ListNode(n%10)
				curr = r
			else:
				curr.next = ListNode(n%10)
				curr = curr.next
			n=n/10
		if n:
			curr.next = ListNode(n%10)
		return r
	

s = Solution()

l1 = ListNode(2)
curr = l1
curr.next = ListNode(4)
curr = curr.next
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(5)

l2 = ListNode(5)
curr = l2
curr.next = ListNode(6)
#curr= curr.next
#curr.next = ListNode(4)

r = s.addTwoNumbers(l1,l2)
while r:
	print r.val
	r=r.next
