# 21. Merge Two Sorted Lists
# Definition for singly-linked list.

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if not l1:
			return l2
		if not l2:
			return l1
		if l1.val<l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2
	
	
So = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

L = So.mergeTwoLists(l1,l2)

while L:
	print L.val
	L = L.next