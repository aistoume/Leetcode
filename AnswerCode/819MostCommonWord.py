# 819 Most Common Word

import re
class Solution(object):
	def mostCommonWord(self, paragraph, banned):
		count = 0
		w = ''
		paragraph = paragraph.lower()
		string = re.sub("[\.\!,\'?;]", "", paragraph).split(' ')
		Lib = {}
		for word in string:
			if word in Lib:
				Lib[word]+=1
			else:
				Lib[word] = 1
			if Lib[word]>count and not word in banned:
				w = word
				count = Lib[word]
		return w
So = Solution()
para = "Bob hit a ball, the hit BALL flew far after it was hit.?!;"
banned = ["hit"]
print So.mostCommonWord(para, banned)
	
	
	