# 242 Valid Anagram
# Youbin Mo 12/27/2017

class Solution(object):
	def isAnagram(self, s, t):
		if not len(s)==len(t):
			return False
		dic = {}
		for i in s:
			if dic.has_key(i):
				dic[i]+=1
			else:
				dic[i]=1
		for i in t:
			if dic.has_key(i):
				dic[i]-=1
			else:
				return False
		for i in dic:
			if not dic[i]==0:
				return False
		return True
	
s = Solution()
S1 = 'car'
S2 = 'rat'

print s.isAnagram(S1,S2)