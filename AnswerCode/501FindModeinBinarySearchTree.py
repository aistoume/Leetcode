# 501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findMode(self, root):
		if not root: return []
		stack = [root]
		Lib = {}
		while stack:
			curr= stack[-1]
			del stack[-1]
			if curr.val in Lib: Lib[curr.val]+=1
			else: Lib[curr.val]=1
			if curr.left: stack.append(curr.left)
			if curr.right: stack.append(curr.right)
		m = max(Lib.values())
		return [i for i in Lib if Lib[i]==m]

So = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(2)
Tree.left.left = TreeNode(3)
Tree.right.right = TreeNode(3)
Tree.left.left.left = TreeNode(4)
Tree.right.right.right = TreeNode(4)

print So.findMode(Tree)