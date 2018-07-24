# 475. Heaters

class Solution(object):
	def findRadius(self, houses, heaters):
		houses.sort()
		heaters.sort()
		rad = -1
		heatpt = 0
		for pos in houses:
			while heaters[heatpt]<= pos and heatpt<len(heaters)-1:heatpt+=1
			toRight = abs(heaters[heatpt]-pos)
			if heatpt>=1:toLeft = abs(heaters[heatpt-1]- pos)
			else: toLeft = toRight
			rad = max(rad,min(toLeft,toRight))
		return rad
So = Solution()
house = [1,3,2,5]
heaters = [2]
print So.findRadius(house,heaters)