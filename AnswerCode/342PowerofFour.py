# 342. Power of Four

class Solution(object):
	def isPowerOfFour(self, num):
		if num==1: return True
		if num<=0: return False
		if not num%4: return self.isPowerOfFour(num/4)
		return False
		
So = Solution()
num = 5
print So.isPowerOfFour(num)