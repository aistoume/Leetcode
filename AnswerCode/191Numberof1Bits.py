# 191. Number of 1 Bits

class Solution(object):
	def hammingWeight(self, n):
		return (bin(n)[2:]).count('1')
		
So = Solution()
n = 128
print So.hammingWeight(n)