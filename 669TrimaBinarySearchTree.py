# Youbin Mo 11/22/2017

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def trimBST(self, root, L, R):
		if root == None:
			return root
		if root.val <= R and root.val >=L:
			root.left = self.trimBST(root.left, L, R)
			root.right = self.trimBST(root.right, L, R)
			return root
		elif root.val<L:
			root = self.trimBST(root.right, L, R)
			return root
		elif root.val >R:
			root = self.trimBST(root.left, L, R)
			return root
		else: 
			return None
		
Tree = TreeNode(1)
Tree.left = TreeNode(0)
Tree.right = TreeNode(2)
print Tree.val
s = Solution()
r = s.trimBST(Tree, 1, 2)
print Tree.val, Tree.right.val