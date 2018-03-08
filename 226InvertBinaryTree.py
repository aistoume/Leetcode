### Youbin 2017/06/22
### 226 Invert Binary Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		if root== None:
			return root
		que = deque([root])
		while (len(que)>0):
			curr = que.popleft()
			if curr.left!=None:
				que.append(curr.left)
			if curr.right!=None:
				que.append(curr.right)
			buff = curr.left
			curr.left = curr.right
			curr.right = buff
		return root
        
t1 = TreeNode(1)
curr =  t1
newNode = TreeNode(3)
curr.left = newNode
newNode = TreeNode(2)
curr.right = newNode
curr = curr.left
newNode = TreeNode(5)
curr.left = newNode