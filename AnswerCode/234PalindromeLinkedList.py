# 234. Palindrome Linked List

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def isPalindrome(self, head):
		L = []
		curr = head
		while curr:
			L.append(curr.val)
			curr = curr.next
		return L==L[::-1]
	
So = Solution()
List = [5,6,6,5]

head = ListNode(List[0])
del List[0]
curr= head
while List:
	curr.next = ListNode(List[0])
	curr = curr.next
	del List[0]
	
print So.isPalindrome(head)