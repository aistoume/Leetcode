# 447. Number of Boomerangs

class Solution:
	def numberOfBoomerangs(self, points):
		count = 0
		Lib = {}
		for i in range(len(points)-1):
			for j in range(i+1,len(points)):
				dist = (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
				if dist in Lib:
					Lib[dist].append((i,j))
				else:
					Lib[dist] = [(i,j)]
		for same in Lib.values():
			for i in range(len(same)-1):
				for j in range(i+1,len(same)):
					if len(set(same[i]+same[j]))==3:
						count+=2	
		return count
		
	
	
So = Solution()
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print So.numberOfBoomerangs(points)