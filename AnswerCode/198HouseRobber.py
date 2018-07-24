# 198 House Robber

class Solution(object):
	def rob(self, nums):
		if not nums: return 0
		buff= [0,nums[0]]
		for i in nums[1:]:
			buff.append(max(buff[-1],buff[-2]+i))
		return buff[-1]
		
So = Solution()
input = [2,7,9,3,1]

print So.rob(input)