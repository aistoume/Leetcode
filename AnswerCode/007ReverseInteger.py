# 7. Reverse Integer

class Solution(object):
	def reverse(self, x):
		s = str(abs(x))[::-1]
		if x<0: s = '-'+s
		if not -2**31<=int(s)<=2**31-1: return 0
		return int(s)
	
So = Solution()
x = -123
print So.reverse(x)