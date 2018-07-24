# 441. Arranging Coins

import math
class Solution(object):
	def arrangeCoins(self, n):
		return int((math.sqrt(1+8*n)-1)/2)
		
So = Solution()
n = 8
print So.arrangeCoins(n)