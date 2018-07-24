# 405. Convert a Number to Hexadecimal

class Solution(object):
	def convertToBase7(self, num):
		if num==0: return "0"
		lib = "0123456789abcdef"
		ans = ""
		while num:
			
		if abs(num)<1:
			return str(num)
		si = num/abs(num)
		return self.convertToBase7(si*(abs(num)/7))+str(abs(num)%7)
		
So = Solution()
num = -1
print So.convertToBase7(num)