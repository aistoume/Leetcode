# 387 First Unique Character in a String
# Youbin Mo 12/21/2017

class Solution(object):
	def firstUniqChar(self, s):
		pool1 = set([])
		pool2 = set([])
		M = [True for i in range(len(s))]
		for i in range(len(s)):
			if s[i] in pool1:
				M[i] = False
			else:
				pool1.add(s[i])
		for i in range(len(s)-1,-1,-1):
			if s[i] in pool2:
				M[i] = False
			else:
				pool2.add(s[i])
		if True in M: return M.index(True)
		return -1	
	
	
s = Solution()
st = "cc"

print s.firstUniqChar(st)