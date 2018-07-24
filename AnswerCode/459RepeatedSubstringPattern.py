# 459. Repeated Substring Pattern

class Solution(object):
	def repeatedSubstringPattern(self, s):
		i,n = 1,len(s)
		if n<2: return False
		while i <=(n/2):
			index = s[i:].find(s[0])
			if index==-1: return False
			if not n%(index+i) and s[:i]*(n/(index+i))==s:
				return True
			i+=1
		return False
			
So = Solution()
s = "ab"
print So.repeatedSubstringPattern(s)