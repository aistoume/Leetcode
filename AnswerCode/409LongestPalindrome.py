# 409. Longest Palindrome

class Solution(object):
	def longestPalindrome(self, s):
		Lib = {}
		for c in s:
			if c in Lib:
				Lib[c]+=1
			else:
				Lib[c]=1
		Single = 0
		count = 0
		for val in Lib.values():
			ad = 2*(val/2)
			count+= ad
			Single = max(Single, val-ad)
		return count+Single
			
So = Solution()
input = "dccaccd"
print So.longestPalindrome(input)
