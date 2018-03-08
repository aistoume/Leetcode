# 404 Sum of Left Leaves
# Youbin Mo 12/21/2017

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sumOfLeftLeaves(self, root):
		Su = 0
		if not root:
			return 0
		stack = [root]
		while stack:
			curr = stack.pop()
			if curr.left:
				stack.append(curr.left)
				if not curr.left.left and not curr.left.right:
					Su+=curr.left.val
			if curr.right:
				stack.append(curr.right)
		return Su
	
	
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print s.sumOfLeftLeaves(root)