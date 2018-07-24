# 202. Happy Number

class Solution(object):
	def isHappy(self, n):
		pool =[]
		while not n in pool:
			Sum = 0
			res = n
			while res:
				Sum+= (res%10)**2
				res = res/10
			if Sum==1:
				return True
			pool.append(n)
			n = Sum
		return (n==1)
			
		
	
So = Solution()
input = 19

print So.isHappy(input)