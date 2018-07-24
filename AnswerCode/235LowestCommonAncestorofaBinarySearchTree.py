# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		stack = [(root,[root])]
		p_flag = q_flag = False
		while stack and not (p_flag and q_flag):
			curr,path = stack[-1]
			del stack[-1]
			if curr == p: p_path = path
			if curr == q: q_path = path
			if curr.left: stack.append((curr.left, path+[curr.left]))
			if curr.right: stack.append((curr.right, path+[curr.right]))
		return [node for node in p_path if node in q_path][-1]
		
		
So = Solution()
Tree = TreeNode(6)
Tree.left = TreeNode(2)
Tree.right = TreeNode(8)
Tree.left.left = TreeNode(0)
Tree.left.right = TreeNode(4)
Tree.left.right.left = TreeNode(3)
Tree.left.right.right = TreeNode(5)
Tree.right.left = TreeNode(7)
Tree.right.right = TreeNode(9)

print So.lowestCommonAncestor(Tree, Tree.left, Tree.right).val