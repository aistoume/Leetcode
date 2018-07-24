# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		if not (headA and headB): return None
		currA,currB = headA,headB
		m=n=0
		while currA.next:
			currA = currA.next
			m+=1
		while currB.next:
			currB = currB.next
			n+=1
		if not currA==currB: return None
		if m>n: currA,currB = headA,headB
		else: currA,currB = headB,headA
		for i in range(abs(m-n)): currA = currA.next
		while not currA==currB: currA,currB = currA.next,currB.next
		return currA
	
List = [1,2,3,4,5,6]	
headA = ListNode(List[0])
del List[0]
curr= headA
while List:
	curr.next = ListNode(List[0])
	if List[0]==4: ITNode = curr
	curr = curr.next
	del List[0]

List = [7,8]
headB = ListNode(List[0])
del List[0]
curr= headB
while List:
	curr.next = ListNode(List[0])
	curr = curr.next
	del List[0]
curr.next = ITNode
So = Solution()
print So.getIntersectionNode(headA,headB)