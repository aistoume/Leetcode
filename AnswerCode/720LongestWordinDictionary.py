# 720. Longest Word in Dictionary

class Solution(object):
	def longestWord(self, words):
		if words ==[]: return ""
		words.sort()
		Lib = {}
		Lib[1] = [w for w in words if len(w)==1]
		for w in words:
			prefix = w[:-1]
			if len(prefix) in Lib and prefix in Lib[len(prefix)]:
				if len(w) in Lib:
					Lib[len(w)].append(w)
				else:
					Lib[len(w)] = [w]
		return (Lib.values()[-1])[0]
				
So = Solution()
words = ["a","ab","o","u","in","banana", "app", "appl", "ap", "apply", "apple"]
words = []
print So.longestWord(words)