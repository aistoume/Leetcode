# 654. Maximum Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def constructMaximumBinaryTree(self, nums):
		if not len(nums):return None
		m = max(nums)
		idx = nums.index(m)
		root = TreeNode(m)
		root.left = self.constructMaximumBinaryTree(nums[:idx])
		root.right = self.constructMaximumBinaryTree(nums[idx+1:])
		return root
	
So = Solution()
nums = [3,2,1,6,0,5]
root = So.constructMaximumBinaryTree(nums)
stack = [root]
while stack:
	curr= stack[0]
	if curr.left:
		stack.append(curr.left)
	if curr.right:
		stack.append(curr.right)
	print curr.val
	del stack[0]