# 367. Valid Perfect Square

class Solution(object):
	def isPerfectSquare(self, num):
		if num==1: return True
		factor = 2
		while factor < num/factor:
			if not num%(factor**2): return self.isPerfectSquare(num/(factor**2))
			factor+=1
		return num==factor**2	
		
So = Solution()
num = 16
print So.isPerfectSquare(num)