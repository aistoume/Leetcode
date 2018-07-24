# 326. Power of Three

class Solution(object):
	def isPowerOfThree(self, n):
		if n==0: return False
		if n==1 or n==3: return True
		if n%3==0: return self.isPowerOfThree(n/3)
		else: return False
	
So = Solution()
n = 2
print So.isPowerOfThree(n)