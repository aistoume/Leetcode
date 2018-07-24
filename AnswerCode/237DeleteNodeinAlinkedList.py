# 237. Delete Node in a Linked List

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, node):
		node.val = node.next.val
        node.next = node.next.next
So = Solution()
L = [4,5,1,9]
head = ListNode(4)
del L[0]
while L:
	curr = head
	newNode = ListNode(L[0])
	curr.next = newNode
	curr = newNode
	del L[0]

So.deleteNode(head)

	
	
	