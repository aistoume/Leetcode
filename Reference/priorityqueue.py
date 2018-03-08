# Priority Queue

from queue import PriorityQueue as pque

pq = pque()
pq.put((5,1))
pq.put((8,2))
pq.put((1,3))
pq.put((2,4))

while not pq.empty():
	node,name = pq.get()
	print 'name=', name, 'node=', node
