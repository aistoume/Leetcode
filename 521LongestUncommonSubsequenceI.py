### Youbin 2017/06/21
### 521 Longest Uncommon Subsequence I

class Solution(object):
    def findLUSlength(self, a, b):
		ma = -1
		for i in range(len(a)):
			for j in range(i+1,len(a)+1):
				s1 = a[i:j]
				if not (s1 in b):
					ma = max(ma, len(s1))
					
		for i in range(len(b)):
			for j in range(i+1,len(b)+1):
				s1 = b[i:j]
				if not (s1 in a):
					ma = max(ma, len(s1))
		return ma
		
		
s = Solution()
L1 = "aefawfawfawfaw"
L2 = "aefawfeawfwafwaef"

r = s.findLUSlength(L1,L2)
print r
print (L1[0:1])
