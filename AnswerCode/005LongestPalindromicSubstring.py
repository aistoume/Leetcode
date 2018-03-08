# 5 Longest Palindromic Substring
# Youbin Mo 12/20/2017

class Solution(object):
	def longestPalindrome(self, s):
		N = len(s)
		M = [[False]*N for i in range(N)]
		p = ''
		for i in range(N):
			M[i][i] = True
			if i+1<N and s[i] == s[i+1]:
				M[i][i+1] = True
			
		for i in range(N-1,0,-1):
			for j in range(i,N-1):
				if M[i][j] and s[i-1]==s[j+1]:
					M[i-1][j+1]=True
						
		for i in range(N):
			for j in range(N):
				if M[i][j] and j-i+1>len(p):
					p = s[i:j+1]
		return p
		
		
			
		
s = Solution()
st = 'cbb'
r = s.longestPalindrome(st)
print r