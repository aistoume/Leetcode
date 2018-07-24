# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		if root == None:
			return []
		stack = [(root,0)]
		Lib = {}
		while stack:
			curr,level = stack[0]
			if not level in Lib:
				Lib[level] = [curr.val]
			else:
				Lib[level].append(curr.val)
			if curr.left:
				stack.append((curr.left,level+1))
			if curr.right:
				stack.append((curr.right,level+1))
			del stack[0]
		L = []
		for node in Lib:
			L.append(Lib[node])
		return L[::-1]
	
	
So = Solution()
Tree = TreeNode(3)
Tree.left = TreeNode(9)
Tree.right = TreeNode(20)
Tree.right.left = TreeNode(15)
Tree.right.right = TreeNode(7)

print So.levelOrderBottom(Tree)