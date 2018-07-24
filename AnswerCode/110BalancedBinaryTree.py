# 110. Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isBalanced(self, root):
		if not root: return True
		if self.isBalanced(root.left) and self.isBalanced(root.right):
			return abs(self.treeDeep(root.left)-self.treeDeep(root.right))<=1
		else: return False
	def treeDeep(self, root):
		if not root: return 0
		return max(self.treeDeep(root.left),self.treeDeep(root.right))+1

		
So = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(2)
Tree.left.left = TreeNode(3)
Tree.right.right = TreeNode(3)
Tree.left.left.left = TreeNode(4)
Tree.right.right.right = TreeNode(4)
print So.isBalanced(Tree)