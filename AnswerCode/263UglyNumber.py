# 263. Ugly Number

class Solution(object):
	def isUgly(self, num):
		if num<=0: return False
		if num==1: return True
		if not num%2: return self.isUgly(num/2)
		elif not num%3: return self.isUgly(num/3)
		elif not num%5: return self.isUgly(num/5)
		else: return False
	
So = Solution()
num = 14
print So.isUgly(num)