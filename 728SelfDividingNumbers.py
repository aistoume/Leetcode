### Youbin Mo 11/21/2017
### 728 Self Dividing Numbers

class Solution(object):
	def selfDividingNumbers(self, left, right):
		L = [p for p in range(left, right+1) if self.checkDividing(p)]
		return L
	
	def checkDividing(self, num):
		a = num
		while a:
			b = a%10
			a = a/10
			if b == 0:
				return False
			else:
				if not num%b ==0:
					return False
		return True
				
		
		
		
s = Solution()

left = 1
right = 22
r = s.selfDividingNumbers(left,right)

print r