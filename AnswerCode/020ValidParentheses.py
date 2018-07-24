# 20. Valid Parentheses

class Solution(object):
	def isValid(self, s):
		stack = []
		Lib = {'(':')','{':'}','[':']'}
		for c in s:
			if c in Lib:
				stack.append(c)
			else:
				if stack and Lib[stack[-1]] == c:del stack[-1]
				else: return False
		return not stack
		
So = Solution()
s = "(]"
print So.isValid(s)