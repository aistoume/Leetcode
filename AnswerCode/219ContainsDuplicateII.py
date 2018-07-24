# 219. Contains Duplicate II

class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		Lib = {}
		for i in range(len(nums)):
			if nums[i] in Lib:
				if i - Lib[nums[i]][-1]<=k: return True
				else: Lib[nums[i]].append(i)
			else: Lib[nums[i]] = [i]
		return False
		
So = Solution()
nums = [1,0,1,1]
k = 1
print So.containsNearbyDuplicate(nums,k)