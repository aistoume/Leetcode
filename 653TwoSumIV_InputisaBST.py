# 653 Two Sum IV - Input is a BST
# Youbin Mo


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findTarget(self, root, k):
		st = [root]
		while len(st):
			curr = st.pop()
			if not k==curr.val+curr.val and self.findItem(root,k-curr.val):
				return True
			if curr.left:
				st.append(curr.left)
			if curr.right:
				st.append(curr.right)
		return False
		
	def findItem(self, root, t):
		if root == None:
			return False
		if root.val == t:
			return True
		if t<root.val:
			return self.findItem(root.left,t)
		if t> root.val:
			return self.findItem(root.right,t)
	
	def findTarget2(self, root, k):
		s = self.makeSet(root)
		for i in s:
			if k-i in s and not k-i==i:
				return True
		return False
		
	def makeSet(self, root):
		s = {root.val}
		if root.left:
			s = s.union(self.makeSet(root.left))
		if root.right:
			s = s.union(self.makeSet(root.right))
		return s
		
		
s = Solution()
curr =TreeNode(5)
curr.left = TreeNode(3)
curr.right = TreeNode(6)
curr.left.left = TreeNode(2)
curr.left.right = TreeNode(4)
curr.right.right = TreeNode(7)


r = s.findTarget2(curr,13)

print r