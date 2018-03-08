### Youbin 2017/07/28
### 94 Binary Tree Inorder Traversal

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inorderTraversal(self, root):
		if root == None:
			return []
		List = []
		if root.left!=None:
			List+= self.inorderTraversal(root.left)
		List.append(root.val)
		if root.right!=None:
			List+= self.inorderTraversal(root.right)
		return List

	
l = TreeNode(1)
l.right = TreeNode(2)
l.right.left = TreeNode(3)
s = Solution()
r = s.inorderTraversal(l)
print r