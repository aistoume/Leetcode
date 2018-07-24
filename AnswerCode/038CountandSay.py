# 38. Count and Say

class Solution(object):
	def countAndSay(self, n):
		ans = "1"
		while n>1:
			ans = self.readSeq(ans)
			n-=1
		return ans
	def readSeq(self,s):
		s = s[::-1]
		ans = s[0]
		pt = 0
		for i in range(len(s)):
			if not s[i]==ans[-1]:
				ans+=str(i-pt)+s[i]
				pt = i
		return (ans+str(i-pt+1))[::-1]
		
So = Solution()
n = 6

print So.countAndSay(n)

#print So.readSeq("111221")