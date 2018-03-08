### Youbin 2017/06/29
### 515 Find Largest Value in Each Tree Row


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def largestValues(self, root):
		if root==None:
			return []
		que = deque([[root, 0]])
		List = [root.val]
		while len(que)>0:
			curr = que.popleft()
			currNode = curr[0]
			depth = curr[1]
			try:
				x = List[depth]
			except IndexError:
				List.append(currNode.val)
				x = List[depth]
			if currNode.val > x:
				List[depth] = currNode.val
			if currNode.left !=None:
				que.append([currNode.left, depth+1])
			if currNode.right !=None:
				que.append([currNode.right, depth+1])
		return List
		
		
s = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(3)
Tree.right = TreeNode(2)
Tree.left.left = TreeNode(5)
Tree.left.right = TreeNode(3)
Tree.right.right = TreeNode(9)
r = s.largestValues(Tree)
print r