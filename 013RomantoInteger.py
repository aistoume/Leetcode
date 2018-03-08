# 013 Roman to Integer
# Youbin Mo 12/27/2017

class Solution(object):
	def romanToInt(self, s):
		dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		prev = total = 0
		for i in range(len(s)-1,-1,-1):
			read_val = dic[s[i]]
			if prev > read_val:
				total-=read_val
			else:
				total+=read_val
			prev = read_val
		return total
	
	
s = Solution()
R = 'MCMXCVI'

print s.romanToInt(R)