# 141. Linked List Cycle

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def hasCycle(self, head):
		pt1 = pt2 = head
		while pt1 and pt2:
			pt1 = pt1.next
			if pt2.next: pt2 = pt2.next
			else: return False
			if pt2.next: pt2=pt2.next
			else: return False
			if pt2==pt1: return True
		return False
	
	
So = Solution()
List = [1,2,3,4,5]

head = ListNode(List[0])
del List[0]
curr= head
while List:
	curr.next = ListNode(List[0])
	curr = curr.next
	del List[0]
	
#curr.next = head	

print So.hasCycle(head)