# 101. Symmetric Tree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSymmetric(self, root):
		if root == None or root.left==root.right==None: return True
		que = [(root,0)]
		Lib = {}
		while que:
			curr,lvl = que[0]
			del que[0]
			if not lvl+1 in Lib: Lib[lvl+1]=[]
			if not curr.left:
				Lib[lvl+1].append(None)
			else:
				Lib[lvl+1].append(curr.left.val)
				que.append((curr.left,lvl+1))	
			if not curr.right:
				Lib[lvl+1].append(None)
			else:
				Lib[lvl+1].append(curr.right.val)
				que.append((curr.right,lvl+1))
		for array in Lib.values():
			l = len(array)
			if not array==array[::-1]:
				return False			
		return True
		
So = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(2)
Tree.left.left = TreeNode(3)
Tree.right.left = TreeNode(3)

print So.isSymmetric(Tree)


