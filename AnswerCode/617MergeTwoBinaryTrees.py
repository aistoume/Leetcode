### Youbin 2017/06/19
### 617 Merge Two Binary Trees
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
		if t1 == None:
			return t2
		if t2 == None:
			return t1
		f1 = deque([t1])
		f2 = deque([t2])
		t = TreeNode(None)
		f = deque([t])
		while(len(f)>0):
			curr = f.popleft()
			curr1 = f1.popleft()
			curr2 = f2.popleft()
			if (curr1!=None and curr2!=None):
				curr.val = curr1.val+curr2.val
				if (curr1.left!=None or curr2.left!=None):
					curr.left = TreeNode(None)
					f1.append(curr1.left)
					f2.append(curr2.left)
					f.append(curr.left)
				if (curr1.right!=None or curr2.right!=None):
					curr.right = TreeNode(None)
					f1.append(curr1.right)
					f2.append(curr2.right)
					f.append(curr.right)
				
			elif curr1==None and curr2!=None:
				curr.val = curr2.val
				if (curr2.left!=None):
					curr.left = TreeNode(None)
					f1.append(None)
					f2.append(curr2.left)
					f.append(curr.left)
				if (curr2.right!=None):
					curr.right = TreeNode(None)
					f1.append(None)
					f2.append(curr2.right)
					f.append(curr.right)
			elif curr1!=None and curr2==None:
				curr.val = curr1.val
				if (curr1.left!=None):
					curr.left = TreeNode(None)
					f1.append(curr1.left)
					f2.append(None)
					f.append(curr.left)
				if (curr1.right!=None):
					curr.right = TreeNode(None)
					f1.append(curr1.right)
					f2.append(None)
					f.append(curr.right)
		return t
		
t1 = TreeNode(1)
curr =  t1
newNode = TreeNode(3)
curr.left = newNode
newNode = TreeNode(2)
curr.right = newNode
curr = curr.left
newNode = TreeNode(5)
curr.left = newNode

t2 = TreeNode(2)
curr =  t2
newNode = TreeNode(1)
curr.left = newNode
newNode = TreeNode(3)
curr.right = newNode
curr = curr.left
newNode = TreeNode(4)
curr.right = newNode
t2.right.right = TreeNode(7)

s = Solution()
t=s.mergeTrees(t1,t2)
print t.val