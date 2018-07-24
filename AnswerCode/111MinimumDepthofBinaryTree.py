# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def minDepth(self, root):
		if not root: return 0
		if not (root.left or root.right): return 1
		if root.left and not root.right: return self.minDepth(root.left)+1
		if not root.left and root.right: return self.minDepth(root.right)+1
		return min(self.minDepth(root.left), self.minDepth(root.right))+1
		
	
So = Solution()
Tree = TreeNode(3)
Tree.left = TreeNode(9)
Tree.left.right = TreeNode(10)
Tree.right = TreeNode(20)
Tree.right.left = TreeNode(15)
Tree.right.right = TreeNode(7)

print So.minDepth(Tree)