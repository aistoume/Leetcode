# 581. Shortest Unsorted Continuous Subarray

class Solution(object):
	def findUnsortedSubarray(self, nums):
		st,ed = 0,len(nums)-1
		while st<ed:
			if nums[st]<= nums[st+1]: st+=1
			else: break
		while st<ed:
			if nums[ed]>=nums[ed-1]:ed-=1
			else:break
		if st==ed: return 0
		ed+=1
		M,m = max(nums[st:ed]),min(nums[st:ed])
		st2,ed2 = 0,len(nums)-1
		while st2<=st and nums[st2]<=m:
			st2+=1
		while ed2>=ed and nums[ed2]>=M:
			ed2-=1
		ed2+=1
		return ed2-st2
		
So =  Solution()
nums = [1,3,2,3,3]
print So.findUnsortedSubarray(nums)