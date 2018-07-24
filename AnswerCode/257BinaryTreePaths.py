#257. Binary Tree Paths

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def binaryTreePaths(self, root):
		ans = []
		if not root:
			return ans
		stack = [(root,str(root.val))]
		while stack:
			curr,path = stack[0]
			if not (curr.left or curr.right):
				ans.append(path)
			if curr.left:
				stack.append((curr.left, path+"->"+str(curr.left.val)))
			if curr.right:
				stack.append((curr.right, path+"->"+str(curr.right.val)))
			del stack[0]
		return ans
	
So = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(3)
Tree.left.right = TreeNode(5)

print So.binaryTreePaths(Tree)