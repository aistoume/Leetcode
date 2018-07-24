# 643. Maximum Average Subarray I

class Solution(object):
	def findMaxAverage(self, nums, k):
		m = curr = sum(nums[:k])
		st,ed = 0,k
		while ed<len(nums):
			curr = curr+nums[ed]-nums[st]
			m = max(m,curr)
			st+=1; ed+=1
		return m/float(k)
		
So = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print So.findMaxAverage(nums,k)