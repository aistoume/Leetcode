#543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def diameterOfBinaryTree(self, root):
		if not root: return 0
		def findDeep(node):
			if not node: return 0
			return 1+max(findDeep(node.left), findDeep(node.right))
		return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), findDeep(root.left)+findDeep(root.right))
	
So = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(3)
Tree.left.left = TreeNode(4)
Tree.left.right = TreeNode(5)
Tree.left.left.left = TreeNode(6)
Tree.left.left.right = TreeNode(7)
Tree.left.right.right = TreeNode(8)
Tree.left.right.right.left = TreeNode(9)
print So.diameterOfBinaryTree(Tree)