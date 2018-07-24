# 844. Backspace String Compare

class Solution(object):
	def backspaceCompare(self, S, T):
		s = t = ""
		for c in S:
			if not c=='#':
				s+=c
			else:
				s=s[:-1]
		for c in T:
			if not c=='#':
				t+=c
			else:
				t=t[:-1]
		return t==s
		
		
So = Solution()
S = "ab#c"
T = "ad#c"
print So.backspaceCompare(S,T)
	