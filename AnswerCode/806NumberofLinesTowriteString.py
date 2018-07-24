class Solution(object):
	def numberOfLines(self, widths, S):
		line = 0
		w = 0
		for c in S:
			w+= widths[ord(c)-ord('a')]
			if w>100:
				w = widths[ord(c)-ord('a')]
				line+=1
		return [line+1, w]
S = Solution()
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
Str = "abcdefghijklmnopqrstuvwxyz"
print S.numberOfLines(widths,Str)