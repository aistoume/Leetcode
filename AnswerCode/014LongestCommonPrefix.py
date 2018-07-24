# 14. Longest Common Prefix

class Solution(object):
	def longestCommonPrefix(self, strs):
		if not strs: return ""
		prefix = strs[0]
		for word in strs[1:]:
			if not prefix: return ""
			i = 0
			while i <len(prefix):
				if i >=len(word):
					prefix = prefix[:i]	
				elif not prefix[i] == word[i]: prefix=prefix[:i]
				i+=1
		return prefix
		
So = Solution()
strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print So.longestCommonPrefix(strs)