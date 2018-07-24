# 594. Longest Harmonious Subsequence

class Solution(object):
	def findLHS(self, nums):
		Lib = {}
		ans = 0
		for n in nums:
			if n in Lib: Lib[n]+=1
			else: Lib[n]=1
			if n+1 in Lib: ans=max(ans,Lib[n]+Lib[n+1])
			if n-1 in Lib: ans=max(ans,Lib[n]+Lib[n-1])
		return ans
So = Solution()
input = [1,3,2,2,5,2,3,7]
print So.findLHS(input)