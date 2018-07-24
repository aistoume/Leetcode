# 507. Perfect Number

class Solution(object):
	def checkPerfectNumber(self, num):
		if num==1: return False
		factor = set([1])
		i = 2
		while i**2<num:
			if not num%i:
				factor.add(i)
				factor.add(num/i)
			i+=1
		return sum(factor)==num
			
		
So = Solution()
num = 5
print So.checkPerfectNumber(num)
