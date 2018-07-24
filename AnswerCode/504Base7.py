# 504 Base 7

class Solution(object):
	def convertToBase7(self, num):
		if abs(num)<7:
			return str(num)
		si = num/abs(num)
		return self.convertToBase7(si*(abs(num)/7))+str(abs(num)%7)
		
So = Solution()
num = -1
print So.convertToBase7(num)