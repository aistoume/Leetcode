# 429. N-ary Tree Level Order Traversal

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
		
class Solution(object):
	def levelOrder(self, root):
		if not root: return []
		Lib = {}
		stack = [(root,0)]
		while stack:
			curr,lvl = stack[0]
			del stack[0]
			if lvl in Lib: Lib[lvl].append(curr.val)
			else: Lib[lvl] = [curr.val]
			if curr.children:
				for node in curr.children:
					stack.append((node,lvl+1))
		return Lib.values()
		
			
So = Solution()
root = Node(0,None)
ch1 = Node(1,None)
ch2 = Node(2,None)
ch3 = Node(3,None)
root.children = [ch1,ch2,ch3]
print So.levelOrder(root)


