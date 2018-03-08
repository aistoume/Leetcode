### Youbin 2017/07/28
### 384 Shuffle an Array

from random import shuffle as shf
class Solution(object):
	def __init__(self, nums):
		global oriList,s
		oriList = nums
		s = nums[:]
	def reset(self):
		return oriList
	def shuffle(self):
		shf(s)
		return s
        


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()

print param_1
print param_2