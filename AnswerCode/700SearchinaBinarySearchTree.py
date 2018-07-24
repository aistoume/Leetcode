# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def searchBST(self, root, val):
		if not root: return None
		stack = [root]
		while stack:
			curr = stack[-1]
			del stack[-1]
			if curr.val == val: return curr
			if curr.left: stack.append(curr.left)
			if curr.right: stack.append(curr.right)
		return None
	
So = Solution()
val = 5
Tree = TreeNode(4)
Tree.left = TreeNode(2)
Tree.right = TreeNode(7)
Tree.left.left = TreeNode(1)
Tree.left.right = TreeNode(3)
print So.searchBST(Tree,val)