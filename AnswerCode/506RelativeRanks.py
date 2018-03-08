# 506 Relative Ranks
# Youbin Mo 12/27/2017

class Solution(object):
	def findRelativeRanks(self, nums):
		n = len(nums)
		Rank = [None]*n
		Index = [nums.index(x) for x in sorted(nums)]
		for i in range(n):
			Rank[Index[i]] = str(n-i)
			if n-i==1:
				Rank[Rank.index("1")] = "Gold Medal"
			if n-i==2:
				Rank[Rank.index("2")] = "Silver Medal"
			if n-i==3:
				Rank[Rank.index("3")] ="Bronze Medal"
		return Rank
	
	
s = Solution()
nums = [5,2,3,1,4]
print s.findRelativeRanks(nums)