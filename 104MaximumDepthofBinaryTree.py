### Youbin 2017/06/22
### 104 Maximum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root==None:
			return 0
		currDepth = 1
		stack = [[currDepth,root]]
		max = 0
		while (len(stack)>0):
			pair = stack.pop()
			currDepth = pair[0]
			curr = pair[1]
			if currDepth>max:
				max= currDepth
			if curr.left!=None:
				stack.append([currDepth+1,curr.left])
			if curr.right!=None:
				stack.append([currDepth+1,curr.right])
		return max
		
	
	

t1 = TreeNode(1)
curr =  t1
newNode = TreeNode(3)
curr.left = newNode
newNode = TreeNode(2)
curr.right = newNode
curr = curr.left
newNode = TreeNode(5)
curr.left = newNode

s = Solution()
r =  s.maxDepth(t1)
print r