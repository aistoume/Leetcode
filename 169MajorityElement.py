# 169 Majority Element
# Youbin Mo 12/21/2017

class Solution(object):
	def majorityElement(self, nums):
		n = len(nums)/2.0
		dic = {}
		for i in nums:
			if dic.has_key(i):
				dic[i]+=1
			else:
				dic[i]=1
			if dic[i]>=n:
				return i
	
        
s = Solution()
nums = [1,1,2,3,4,4,5,1,1,1,1,1]
print s.majorityElement(nums)