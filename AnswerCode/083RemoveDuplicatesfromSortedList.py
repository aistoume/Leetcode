# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if not head: return None
		curr = head
		while curr.next:
			if curr.val==curr.next.val:
				curr.next = curr.next.next
			else:
				curr = curr.next
		return head
	
So = Solution()

L = [1,1,2,3,3]
head = ListNode(L[0])
curr = head
for i in L[1:]:
	curr.next = ListNode(i)
	curr = curr.next

ans = So.deleteDuplicates(head)
while ans:
	print ans.val
	ans = ans.next