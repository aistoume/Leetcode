# 027 Remove Element

class Solution(object):
    def removeElement(self, nums, val):
		c = 0
		for i in nums: 
			if i==val:c+=1
		for i in range(c): nums.remove(val)
		return len(nums)

So = Solution()
nums = [3,2,2,3]
val = 2
print So.removeElement(nums,val)