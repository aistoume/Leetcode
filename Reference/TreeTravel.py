# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# Make a Tree
NodeList = [2,4,None,3,7]


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
	
	
Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(2)
Tree.left.left = TreeNode(3)
Tree.right.right = TreeNode(3)
Tree.left.left.left = TreeNode(4)
Tree.right.right.right = TreeNode(4)