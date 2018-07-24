# 172. Factorial Trailing Zeroes

class Solution(object):
	def trailingZeroes(self, n):
		count5 = 0
		while n:
			count5+=n/5
			n = n/5
		return count5
So = Solution()
n = 25
print So.trailingZeroes(n)