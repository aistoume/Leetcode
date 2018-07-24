# 69. Sqrt(x)

class Solution(object):
	def mySqrt(self, x):
		if x<=1: return int(x)
		r = 10**((len(str(x))-1)/2)
		while r**2<=x:
			r+=1
		return r-1
So = Solution()
x = 1000
print So.mySqrt(x)