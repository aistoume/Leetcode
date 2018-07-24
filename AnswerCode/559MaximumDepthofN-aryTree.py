# 559. Maximum Depth of N-ary Tree"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
		if not root: return 0
		if not root.children: return 1
		m = 0
		for ch in root.children:
			m = max(m, self.maxDepth(ch)+1)
		return m
		
So = Solution()
