# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def minDiffInBST(self, root):
		Li = self.getList(root)
		m = 9999
		for i in range(1,len(Li)):
			m = min(m, Li[i]-Li[i-1])
		return m
		
	def getList(self,root):
		if not root:
			return []
		return self.getList(root.left)+[root.val]+self.getList(root.right)

		
So = Solution()
Tree = TreeNode(4)
Tree.left = TreeNode(2)
Tree.left.left = TreeNode(1)
Tree.left.right = TreeNode(3)
Tree.right = TreeNode(6)

print So.minDiffInBST(Tree)