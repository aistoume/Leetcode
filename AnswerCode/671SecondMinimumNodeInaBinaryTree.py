# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findSecondMinimumValue(self, root):
		if root.left == root.right==None:return -1
		if root.left.val==root.val: L = self.findSecondMinimumValue(root.left)
		else: L = root.left.val
		if root.right.val==root.val: R = self.findSecondMinimumValue(root.right)
		else: R = root.right.val
		if L==R==root.val or L==R==-1: return -1
		elif L==root.val or L==-1: return R
		elif R==root.val or R==-1: return L
		else: return min(L,R)
		
			
So = Solution()
Tree = TreeNode(2)
Tree.left = TreeNode(2)
Tree.right = TreeNode(5)
Tree.right.left = TreeNode(5)
Tree.right.right = TreeNode(7)
print So.findSecondMinimumValue(Tree)