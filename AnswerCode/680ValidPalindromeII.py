# 680. Valid Palindrome II

class Solution(object):
	def validPalindrome(self, s):
		st,ed = 0,len(s)-1
		while st<ed:
			if s[st]==s[ed]:
				st+=1
				ed-=1
			else:
				sub1 = s[st:ed] 
				sub2 = s[st+1:ed+1]
				return sub1==sub1[::-1] or sub2==sub2[::-1]
		return True

So = Solution()
s = "eccer"
st,ed = 0,4
print s[st:ed],s[ed-1:st-1:-1]
print s[st+1:ed+1],s[ed:st:-1]
print So.validPalindrome(s)