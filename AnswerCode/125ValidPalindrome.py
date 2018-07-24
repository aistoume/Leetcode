# 125. Valid Palindrome

class Solution(object):
	def isPalindrome(self, s):
		ans = ""
		for c in s:
			if 'A'<=c<='Z' or 'a'<=c<='z' or '0'<=c<='9': ans+=c
		ans= ans.lower()
		return ans==ans[::-1]
		
So = Solution()
s = "A man, a plan, a canal: Panama"
s ="`l;`` 1o1 ??;l`"
print So.isPalindrome(s)