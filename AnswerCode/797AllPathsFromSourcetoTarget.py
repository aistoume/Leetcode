# 797. All Paths From Source to Target


class Solution(object):
	def allPathsSourceTarget(self, graph):
		target = len(graph)-1
		que = [[0]]
		ans = []
		while que:
			path = que.pop()
			node = path[-1]
			if node==target: ans.append(path)
			for neigh in graph[node]:
				que.append(path+[neigh]) 
		return ans
			
		
So = Solution()
graph = [[1,2], [3], [1,3], []]
print So.allPathsSourceTarget(graph)
