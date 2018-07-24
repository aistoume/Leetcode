# 108. Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		if nums ==[]:
			return None
		if len(nums)==1:
			return TreeNode(nums[0])
		i = len(nums)/2
		root = TreeNode(nums[i])
		root.left = self.sortedArrayToBST(nums[0:i])
		if i+1<len(nums):
			root.right = self.sortedArrayToBST(nums[i+1:])
		return root
		
	
	
So = Solution()
input = [-10,-3,0,5,9]
#input = [0,1]
tree = So.sortedArrayToBST(input)

stack = [tree]
while stack:
	curr= stack[0]
	if curr.left:
		stack.append(curr.left)
	if curr.right:
		stack.append(curr.right)
	print curr.val
	del stack[0]
	
