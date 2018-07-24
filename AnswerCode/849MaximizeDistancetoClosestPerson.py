# 849. Maximize Distance to Closest Person

class Solution(object):
	def maxDistToClosest(self, seats):
		dist = start = seats.index(1)
		for pt in range(start,len(seats)):
			if seats[pt]:
				dist = max(dist,(pt-start)/2)
				start = pt
		return max(dist,len(seats)-start-1)
		
So = Solution()
seats = [1,1,0,0,0,1,0]
print So.maxDistToClosest(seats)