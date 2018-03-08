# 001 Two Sum
# Youbin Mo 12/19/2017

class Solution(object):
	def twoSum(self, nums, target):
		s = set(nums)
		a = [[i,nums.index(target-nums[i])] for i in range(len(nums)) if target-nums[i] in s and i<=nums.index(target-nums[i])]
		print a
		for item in a:
			if not item[0]==item[1]:
				return item
			else:
				b = nums[(item[0]+1):]
				if nums[item[0]] in b:
					return [item[0],b.index(target-nums[item[0]])+item[0]+1]
	
	
s = Solution()

r = s.twoSum([3,2,4],6)
print r