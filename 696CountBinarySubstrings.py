# 696 Count Binary Substrings
# Youbin Mo 12/11/2017

class Solution(object):
	def countBinarySubstrings(self, s):
		curr = 1
		count = 0
		prev = 0
		for k in range(1, len(s)):
			if s[k] == s[k-1]:
				curr+=1
			else:
				count+= min(prev,curr)
				prev = curr
				curr = 1
		count+= min(prev,curr)
		return count
				




s = Solution()
bs = '0000111000'	
r = s.countBinarySubstrings(bs)
print r