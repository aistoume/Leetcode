# 693 Binary Number with Alternating Bits
# Youbin Mo 11/26/2017

class Solution(object):
	def hasAlternatingBits(self, n):
		f = n%2
		n = n/2
		while n:
			if (n%2)^f:
				f = n%2
				n = n/2
			else:
				return False
		return True
	
	
s = Solution()
r = s.hasAlternatingBits(11)
print r