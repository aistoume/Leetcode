# 637 Average of Levels in Binary Tree
# Youbin Mo 11/26//2017

# Definition for a binary tree node.

import Queue as que
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def averageOfLevels(self, root):
		q = que.Queue()
		q.put((root,0))
		List = []
		while not q.empty():
			curr,l = q.get()
			if len(List)<=l:
				List.append((curr.val,1))
			else:
				List[l] = (List[l][0]+curr.val, List[l][1]+1)
			if not curr.left==None:
				q.put((curr.left,l+1))
			if not curr.right==None:
				q.put((curr.right, l+1))
		r = []
		for v,n in List:
			r.append(v*1.0/n)
		return r
			
	
	

Tree = TreeNode(1)
Tree.left = TreeNode(0)
Tree.right = TreeNode(2)
print Tree.val
s = Solution()
r = s.averageOfLevels(Tree)
print r