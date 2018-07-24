#812. Largest Triangle Area

class Solution(object):
	def largestTriangleArea(self, points):
		MaxArea = 0
		L = len(points)
		for i in range(L):
			[x1,y1] = points[i]
			for j in range(i+1,L):
				[x2,y2] = points[j]
				for k in range(j+1,L):
					[x3,y3] = points[k]
					MaxArea = max(MaxArea,0.5*abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2))
		return MaxArea


So = Solution()
point = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print So.largestTriangleArea(point)

