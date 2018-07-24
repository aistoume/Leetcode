# 633. Sum of Square Numbers

import math
class Solution(object):
	def judgeSquareSum(self, c):
		for i in range(int(math.sqrt(c))+1):
			b = math.sqrt(c-i**2)
			if b==int(b):return True
		return False
		
So = Solution()
c = 2
print So.judgeSquareSum(c)