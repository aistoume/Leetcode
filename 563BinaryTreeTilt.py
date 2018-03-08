# 563 Binary Tree Tilt
# Youbin Mo 12/22/2017

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findTilt(self, root):
		s,tilt = self.subFind(root)
		return tilt
	def subFind(self,root):
		if not root:
			return 0,0
		l,t_l = self.subFind(root.left)
		r,t_r = self.subFind(root.right)
		return l+r+root.val, t_l+t_r+abs(l-r)
	
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

print s.findTilt(root)