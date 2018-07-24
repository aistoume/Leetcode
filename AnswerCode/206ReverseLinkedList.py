# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, node):
		if node == None:
			return None
		nx = None
		while node.next:
			buff = node.next
			node.next = nx
			nx = node
			node = buff	
		node.next = nx
		return node
			
			
So = Solution()
L = [1,2,3]
head = ListNode(L[0])
del L[0]
curr = head
while L:
	newNode = ListNode(L[0])
	curr.next = newNode
	curr = curr.next
	del L[0]

print "NodeList"
print head.val,head.next.val,head.next.next.val
print "Inverse"
node = So.reverseList(head)
#print node.val
while node:
	print node.val
	node = node.next
	
	
	