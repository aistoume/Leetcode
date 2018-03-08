### Youbin 2017/06/30
### 538 Convert BST to Greater Tree

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def convertBST(self, root):
		sum = 0
		parent = None
		self.Update(root, parent, sum)
		return root
		
	def Update(self, Node, parent, sum):
		curr = Node
		if curr == None:
			return sum
		if curr.right!=None:
			sum = self.Update(curr.right, curr, sum)
		sum += curr.val
		curr.val = sum
		
		if curr.left!=None:
			sum = self.Update(curr.left, curr, sum)
		return sum
		
		
	def printTree(self, root):
		que = deque([root])
		while len(que)>0:
			curr = que.popleft()
			print curr.val
			if curr.left!=None:
				que.append(curr.left)
			if curr.right!=None:
				que.append(curr.right)
		
	
s = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(0)
Tree.right = TreeNode(4)
Tree.left.left = TreeNode(-2)
Tree.right.left = TreeNode(3)

r = s.convertBST(Tree)
s.printTree(r)