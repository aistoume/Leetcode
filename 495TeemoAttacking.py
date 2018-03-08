### Youbin 2017/07/12
### 495 Teemo Attacking

class Solution(object):
	def findPoisonedDuration(self, timeSeries, duration):
		if timeSeries == []:
			return 0
		if duration == 0:
			return 0
			
		sum = 0
		
		for i in range(len(timeSeries)):
			if i == (len(timeSeries)-1):
				sum+= duration
				return sum
			else:
				currTime = timeSeries[i]
				endTime = timeSeries[i]+duration 
				if endTime<=timeSeries[i+1]:
					sum+= duration
				else:
					sum+=(timeSeries[i+1]-currTime)
			
	
	
s = Solution()
l = [1,2]
d = 3
r = s.findPoisonedDuration(l,d)
print r
