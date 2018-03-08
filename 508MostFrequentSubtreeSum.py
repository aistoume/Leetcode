### Youbin 2017/06/30
### 508 Most Frequent Subtree Sum

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def findFrequentTreeSum(self, root):
		if root==None:
			return []
		sum = 0
		parent = None
		self.Update(root, parent)
		que = deque([root])
		dict = {}
		while len(que)>0:
			curr = que.popleft()
			if dict.has_key(curr.val):
				dict[curr.val]+=1
			else:
				dict[curr.val] = 1
			if curr.left!=None:
				que.append(curr.left)
			if curr.right!=None:
				que.append(curr.right)
		k = dict.keys()
		v = dict.values()
		maxCount = max(v)
		reList = [ k[i] for i in range(len(k)) if v[i]==maxCount]
		return reList
		
	def Update(self, Node, parent):
		curr = Node
		if curr == None:
			return 0
		if curr.right!=None:
			self.Update(curr.right, curr)
			curr.val += curr.right.val
			
		if curr.left!=None:
			self.Update(curr.left, curr)
			curr.val += curr.left.val

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
Tree.right.right = TreeNode(3)

r = s.findFrequentTreeSum(Tree)
s.printTree(r)