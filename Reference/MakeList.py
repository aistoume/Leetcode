# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def MakeList(List):
	head = ListNode(List[0])
	del List[0]
	curr= head
	while List:
		curr.next = ListNode(List[0])
		curr = curr.next
	return head
		
		
head = ListNode(List[0])
del List[0]
curr= head
while List:
	curr.next = ListNode(List[0])
	curr = curr.next
	del List[0]