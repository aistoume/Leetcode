# 112. Path Sum

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def hasPathSum(self, root, sum):
		if not root: return False
		if not (root.left or root.right) and root.val == sum: return True
		flag = False
		if root.left: flag = flag or self.hasPathSum(root.left,sum-root.val)
		if root.right: flag = flag or self.hasPathSum(root.right,sum-root.val)
		return flag
		
		
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

n = 3
print So.hasPathSum(Tree,n)