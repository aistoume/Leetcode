# 860. Lemonade Change

class Solution(object):
	def lemonadeChange(self, bills):
		c5,c10= 0,0
		for d in bills:
			if d ==5: c5+=1
			if d == 10: 
				c5-=1
				c10+=1
			if d == 20:
				if c10 ==0:
					c5-=3
				else:
					c5-=1
					c10-=1
			if c5<0 or c10<0:
				return False
		return True
			
	
	
So = Solution()
bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print So.lemonadeChange(bills)