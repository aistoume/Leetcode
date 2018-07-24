# 290. Word Pattern

class Solution(object):
	def wordPattern(self, pattern, str):
		if pattern=="" or str=="": return False
		str = str.split(' ')
		if not len(str)==len(pattern): return False
		Lib = {}
		for i in range(len(pattern)):
			if not pattern[i] in Lib: Lib[pattern[i]]=str[i]
			elif not Lib[pattern[i]]==str[i]: return False
		Lib = {}
		for i in range(len(str)):
			if not str[i] in Lib: Lib[str[i]]=pattern[i]
			elif not Lib[str[i]]==pattern[i]: return False
		return True
	
So = Solution()
pattern = "abba"
str = "dog dog dog dog"
print So.wordPattern(pattern,str)
	