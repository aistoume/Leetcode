# 9. Palindrome Number

class Solution(object):
	def isPalindrome(self, x):
		x = str(x)
		return x==x[::-1]
		
So = Solution()
x = -121
print So.isPalindrome(x)