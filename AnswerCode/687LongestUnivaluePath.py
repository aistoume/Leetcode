# 687. Longest Univalue Path

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
		
class Solution(object):
	def longestUnivaluePath(self, root):
		if not root: return 0
		deepL = subL = deepR = subR = 0
		if root.left: 
			subL = self.longestUnivaluePath(root.left)
			if root.val == root.left.val:
				deepL = 1+self.deepOfUPath(root.left)
		if root.right:
			subR = self.longestUnivaluePath(root.right)
			if root.val == root.right.val:
				deepR = 1+self.deepOfUPath(root.right) 
		return max(deepL+deepR, subL, subR)
		
	def deepOfUPath(self,root):
		if not (root): return 0
		if (root.left) and root.val == root.left.val: L = 1+self.deepOfUPath(root.left)
		else: L = 0
		if (root.right) and root.val == root.right.val: R = 1+self.deepOfUPath(root.right)
		else: R = 0
		return max(L,R)
So = Solution()
Tree = TreeNode(5)
Tree.left = TreeNode(4)
Tree.right = TreeNode(5)
Tree.left.left = TreeNode(1)
Tree.left.right = TreeNode(1)
Tree.right.right = TreeNode(5)

print So.longestUnivaluePath(Tree)