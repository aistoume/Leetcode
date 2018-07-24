# 28. Implement strStr()

class Solution(object):
	def strStr(self, haystack, needle):
		if needle in haystack: return haystack.find(needle)
		else: return -1
So = Solution()
haystack = "hello"
needle = "llk"
print So.strStr(haystack,needle)