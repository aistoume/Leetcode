### Youbin 2017/06/20
### 485 Max Consecutive Ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
		max = 0
		count = 0
		for i in nums:
			if i == 1:
				count += 1
			else:
				if count > max:
					max = count
				count = 0
		if count >  max:
			max = count
		return max
		
		
s = Solution()
l = [1,1,0,1,1,1]
r = s.findMaxConsecutiveOnes(l)
print r