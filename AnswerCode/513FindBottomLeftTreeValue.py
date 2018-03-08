### Youbin 2017/06/25
### 513 Find Bottom Left Tree Value

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findBottomLeftValue(self, root):
		que = deque([[root,0]])
		List = [[root.val, 0]]
		MaxDepth = 0
		while len(que)>0:
			curr = que.popleft()
			depth = curr[1]
			currNode = curr[0]
			if currNode.left!=None:
				que.append([currNode.left, depth+1])
				if depth+1>=MaxDepth:
					List.append([currNode.left.val, depth+1])
					MaxDepth = depth+1
			if currNode.right!=None:
				que.append([currNode.right, depth+1])
				if depth+1>=MaxDepth:
					List.append([currNode.right.val, depth+1])
					MaxDepth = depth+1
		for pair in List:
			if pair[1] == MaxDepth:
				return pair[0]
		
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.right = TreeNode(3)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.right.left = TreeNode(7)

s = Solution()
r = s.findBottomLeftValue(tree)
print r

