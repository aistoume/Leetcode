# 3 Longest Substring Without Repeating Characters
# Youbin Mo 12/19/2017


class Solution(object):
	def lengthOfLongestSubstring(self, s):
		N = len(s)
		M =0
		L = [0]*(N+1)
		L[N] = N

		while N>0:
			sub = s[N:L[N]]
			print sub
			if s[N-1] in sub:
				L[N-1] = N + sub.index(s[N-1])
				print L[N-1]
			else:
				L[N-1] = L[N]
			
			if L[N-1]-N+1>M:
				M = L[N]-N+1
			N-=1
		return M


s = Solution()
string = 'abcd'
string = 'c'
r = s.lengthOfLongestSubstring(string)
print r