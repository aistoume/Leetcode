### Youbin
from collections import deque

class Node(object):
	def __init__(self, name):
		self.name = name
		self.count = 0
		self.pointer = [None, None, None, None]

	def build(self, text):
		#pointer order : ATCG
		orderTable = "ATCG"
		curr = self
		for i in range(len(text)):
			n = orderTable.index(text[i])
			prev = text[0:i+1]
			#print n, prev
			if curr.pointer[n] ==None:
				curr.pointer[n] = Node(prev)
				curr = curr.pointer[n]
				curr.count+=1
			else:
				curr = curr.pointer[n]
				curr.count+=1
		
	def printTree(self):
		que = deque([self])
		while (len(que)>0):
			curr = que.popleft()
			print curr.name, ':', curr.count
			for i in range(4):
				if curr.pointer[i]!=None:
					que.append(curr.pointer[i])
text = "ACTCGT"
root = Node("ROOT")
for i in range(len(text)):
	root.build(text[i:len(text)])

root.printTree()

	