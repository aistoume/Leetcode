# 58. Length of Last Word

class Solution(object):
	def lengthOfLastWord(self, s):
		flag = False
		ed = 0
		pt = len(s)-1
		while pt>=0:
			if 'A'<=s[pt]<='z' and not flag:
				flag = True
				ed = pt
			if flag and not 'A'<=s[pt]<='z': return ed-pt
			pt-=1
		return ed+int(flag)
			
		
		
So = Solution()
s = "Hello World%!#$#@$%@$ "
print So.lengthOfLastWord(s)