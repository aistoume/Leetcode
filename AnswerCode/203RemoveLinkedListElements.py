# 203. Remove Linked List Elements

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def removeElements(self, head, val):
		while head and head.val==val:
			head = head.next
		curr = head
		while curr:
			if curr.next and curr.next.val==val: curr.next = curr.next.next
			else: curr = curr.next
		return head
			
	
So = Solution()
List = [6,6,6,5]

head = ListNode(List[0])
del List[0]
curr= head
while List:
	curr.next = ListNode(List[0])
	curr = curr.next
	del List[0]

val = 6
head = So.removeElements(head,6)
curr = head
while curr:
	print curr.val
	curr= curr.next