# 541. Reverse String II

class Solution(object):
	def reverseStr(self, s, k):
		if len(s)<k:
			return s[::-1]
		elif k<=len(s)<2*k:
			return s[k-1::-1]+s[k:]
		else:
			return s[k-1::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k)
		
	
So = Solution()
s = "abcdefg"
k = 2

print So.reverseStr(s,k)