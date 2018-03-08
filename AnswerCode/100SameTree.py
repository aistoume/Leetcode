# 100 Same Tree
# Youbin Mo 12/22/2017

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		if not p or not q:
			return False
		if p.val == q.val:
			return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
		else:
			return False
			
	
	
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(4)
root2.left = TreeNode(3)
root.right = TreeNode(5)

print s.isSameTree(root,root)