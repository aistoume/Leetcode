# 458. Poor Pigs

import math

class Solution(object):
	def poorPigs(self, buckets, minutesToDie, minutesToTest):
		return int(math.ceil(math.log(buckets,(minutesToTest/minutesToDie+1))))
	

So = Solution()
b,mDie,mTest = 1000,15,60
print So.poorPigs(b,mDie,mTest)