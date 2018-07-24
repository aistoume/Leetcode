# 572. Subtree of Another Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def isSubtree(self, s, t):
		def convertStr(node):
			return "^"+str(node.val)+"#"+convertStr(node.left)+convertStr(node.right) if node else "$"
		return convertStr(t) in convertStr(s)

So = Solution()
Tree = TreeNode(3)
Tree.left = TreeNode(4)
Tree.right = TreeNode(5)
Tree.left.left = TreeNode(1)
Tree.left.right = TreeNode(2)


t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

print So.isSubtree(Tree.left.right,t.left.left)