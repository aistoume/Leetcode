# 814. Binary Tree Pruning

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def pruneTree(self, root):
		if not root: return None
		if root.left: root.left = self.pruneTree(root.left)
		if root.right: root.right = self.pruneTree(root.right)
		if root.val ==0 and not (root.left or root.right): return None
		return root
So = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(0)
Tree.right = TreeNode(1)
Tree.left.left = TreeNode(0)
Tree.left.right = TreeNode(0)
Tree.right.left = TreeNode(0)
Tree.right.right = TreeNode(1)
tree = So.pruneTree(Tree)

# Print Tree
stack = [tree]
while stack:
	curr= stack[0]
	if curr.left:
		stack.append(curr.left)
	if curr.right:
		stack.append(curr.right)
	print curr.val
	del stack[0]