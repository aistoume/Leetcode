# Youbin Mo 11/22/2017
# 682 Baseball Game

class Solution(object):
	def calPoints(self, ops):
		stack = []	
		for m in ops:
			if m == '+':	
				stack.append(stack[-1]+stack[-2])
			elif m == 'D':
				stack.append(stack[-1]*2)
			elif m == 'C':
				stack.pop()
			else:
				stack.append(int(m))				
		return sum(stack)
		
		
		
s = Solution()
score = ["5","2","C","D","+"]
score = ["5","-2","4","C","D","9","+","+"]
r = s.calPoints(score)

print r

