# 190. Reverse Bits

class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		b = bin(n)
		return int(b[:1:-1] +"0"*(34-len(b)),2)
So = Solution()
n = 43261596
print So.reverseBits(n)