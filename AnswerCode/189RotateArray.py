# 189. Rotate Array

class Solution(object):
	def rotate(self, nums, k):
		while k:
			buff = nums[-1]
			del nums[-1]
			nums.insert(0,buff)
			k-=1
			
So = Solution()
nums = [-1,-100,3,99]
k = 2
So.rotate(nums,k)
print nums