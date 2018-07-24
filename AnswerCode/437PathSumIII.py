# 437. Path Sum III

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		if not root: return 0
		return self.checkSum(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
	def checkSum(self, root, sum):
		if root==None: return 0
		path = self.checkSum(root.left,sum-root.val)+self.checkSum(root.right,sum-root.val)
		if root.val==sum: path+=1
		return path
		
		
So = Solution()
Tree = TreeNode(10)
Tree.left = TreeNode(5)
Tree.right = TreeNode(-3)
Tree.left.left = TreeNode(3)
Tree.left.right = TreeNode(2)
Tree.left.left.left = TreeNode(3)
Tree.left.left.right = TreeNode(-2)
Tree.left.right.right = TreeNode(1)
Tree.right.right = TreeNode(11)
n = 11
print So.pathSum(Tree,n)