# 438. Find All Anagrams in a String

class Solution(object):
	def findAnagrams(self, s, p):
		if len(s)<len(p): return []
		Lib = {}
		for c in p:
			if c in Lib: Lib[c]+=1
			else: Lib[c]=1
		for c in s[:len(p)]:
			if c in Lib: Lib[c]-=1
		if set(Lib.values())==set([0]): ans =[0]
		else: ans = []
		pt = 0
		while pt+len(p)<len(s):
			if s[pt] in Lib: Lib[s[pt]]+=1
			if s[pt+len(p)] in Lib: Lib[s[pt+len(p)]]-=1
			if set(Lib.values())==set([0]): ans.append(pt+1)
			pt+=1
		return ans
So = Solution()
s = "cbaebabacd"
p = "abc"
print So.findAnagrams(s,p)