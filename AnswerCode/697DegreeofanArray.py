# 697 Degree of an Array
# Youbin Mo 12/27/2017

class Solution(object):
	def findShortestSubArray(self, nums):
		if len(nums)<2:	return len(nums)
		dic = {}
		for i in range(len(nums)):
			n = nums[i]
			if dic.has_key(n):
				dic[n][0] +=1 
				dic[n][2] = i
			else:
				dic[n]=[1,i,i]
		degree = max(dic[i][0] for i in dic)
		waitList = []
		for i in dic:
			if dic[i][0]==degree:
				waitList.append(i)
		print waitList
		smallLen = len(nums)
		for i in waitList:
			if dic[i][2]-dic[i][1]+1<smallLen:
				smallLen = dic[i][2]-dic[i][1]+1
		return smallLen

s = Solution()
nums = [1,2,2,1,2,1,1,1,1,2,2,2]
print s.findShortestSubArray(nums)