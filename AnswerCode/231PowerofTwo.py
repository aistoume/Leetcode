# 231. Power of Two

class Solution(object):
	def isPowerOfTwo(self, n):
		if n==0: return False
		if n==1 or n==2: return True
		if n%2==0: return self.isPowerOfTwo(n/2)
		else: return False
	
So = Solution()
n = 0
print So.isPowerOfTwo(n)