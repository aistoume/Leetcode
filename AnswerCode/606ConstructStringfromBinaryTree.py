### Youbin 2017/06/22
### 606 Construct String from Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def tree2str(self, t):
		if not t:
			return ""
		L = str(t.val)
		if t.left==None and t.right==None:
			return L
		L+="("
		if t.left:
			L+=self.tree2str(t.left)
		L+=")"
		if t.right:
			L+="("+self.tree2str(t.right)+")"
		
		return L
			
		
s = Solution()
t1 = TreeNode(1)
curr =  t1
newNode = TreeNode(2)
curr.left = newNode
newNode = TreeNode(3)
curr.right = newNode
curr = curr.left
newNode = TreeNode(4)
curr.right = newNode

r = s.tree2str([])

print r
