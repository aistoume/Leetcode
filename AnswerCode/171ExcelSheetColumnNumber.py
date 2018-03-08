# 171 Excel Sheet Column Number
# Youbin Mo 12/22/2017

class Solution(object):
	def titleToNumber(self, s):
		n = 1
		Num = 0
		s = list(s)
		while s:
			l = s.pop()
			Num+= (ord(l)-64)*n
			n*=26
		return Num
	
	
s = Solution()
st = "B"

print s.titleToNumber(st)