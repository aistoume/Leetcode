### Youbin 2017/07/17
### 623 Add One Row to Tree

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def addOneRow(self, root, v, d):
		if d == 1:
			newNode = TreeNode(v)
			newNode.left = root
			return newNode
		else:
			que = deque([(1,root)])
			while (len(que)>0):
				curr = que.popleft()
				depth = curr[0]
				currNode = curr[1]
				if currNode.left !=None:
					que.append((depth+1,currNode.left))
				if currNode.right != None:
					que.append((depth+1,currNode.right))
				if depth == d-1:
					if currNode.left !=None: 
						newNode = TreeNode(v)
						newNode.left = currNode.left
						currNode.left = newNode
					else:
						currNode.left = TreeNode(v)
					if currNode.right !=None:
						newNode = TreeNode(v)
						newNode.right = currNode.right
						currNode.right = newNode
					else:
						currNode.right = TreeNode(v)
			return root
				

	def printTree(self, root):
		que = deque([root])
		while (len(que)>0):
			curr = que.popleft()
			print curr.val
			if curr.left !=None:
				que.append(curr.left)
			if curr.right != None:
				que.append(curr.right)
			
	
s = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(0)
Tree.right = TreeNode(4)
Tree.left.left = TreeNode(-2)
Tree.right.left = TreeNode(3)

r = s.addOneRow(Tree,10,2)
s.printTree(r)