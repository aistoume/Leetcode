# 205. Isomorphic Strings

class Solution(object):
	def isIsomorphic(self, s, t):
		if s==t: return True
		Lib= {}
		for i in range(len(s)):
			if not s[i] in Lib: Lib[s[i]] = t[i]
			elif not Lib[s[i]] == t[i]: return False
		Lib= {}
		for i in range(len(t)):
			if not t[i] in Lib: Lib[t[i]] = s[i]
			elif not Lib[t[i]] == s[i]: return False
		return True
So = Solution()
s = ""
t = ""
print So.isIsomorphic(s,t)