# 628. Maximum Product of Three Numbers

class Solution(object):
	def maximumProduct(self, nums):
		nums.sort()
		return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
	
So = Solution()
input = [-5,1,2,3,4,-9,-2]
print So.maximumProduct(input)
