# 268. Missing Number

class Solution(object):
	def missingNumber(self, nums):
		m = max(nums)
		ans = (m*(m+1)/2-sum(nums))
		if ans ==0:
			if 0 in nums:
				return len(nums)
			else:
				return 0
		return ans
		
	
So = Solution()
input = [0,1,2,4]
print So.missingNumber(input)