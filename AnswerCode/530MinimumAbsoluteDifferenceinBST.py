### Youbin 2017/06/23
### 530 Minimum Absolute Difference in BST

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def getMinimumDifference(self, root):
		if not root: return None
		if not root.left and not root.right:
			return None
		m,M,diff = self.getMinMax(root)
		return diff
		
	def getMinMax(self, root):
		if not root.left and not root.right:
			return root.val,root.val,10**7 # min, max, diff
		diff = 10**7
		m_l,M_r = 10**7,-1
		if root.left:
			m_l,M_l,diff_l = self.getMinMax(root.left)
			diff = min(diff,diff_l,root.val-M_l)
		if root.right:
			m_r,M_r,diff_r = self.getMinMax(root.right)
			diff = min(diff,diff_r,m_r-root.val)
		return min(m_l,root.val),max(M_r,root.val), diff
		
		
tree = TreeNode(1)
tree.right = TreeNode(3)
tree.right.left = TreeNode(2)
s = Solution()
print s.getMinimumDifference(tree)
