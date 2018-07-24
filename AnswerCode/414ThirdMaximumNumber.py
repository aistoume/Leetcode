# 414. Third Maximum Number

class Solution(object):
	def thirdMax(self, nums):
		nums = set(nums)
		if len(nums)<3: return max(nums)
		ans = []
		while nums:
			k = nums.pop()
			if len(ans)<3 or k>min(ans): ans.append(k)
			ans.sort()
			while len(ans)>3: del ans[0]
		return ans[0]
	
So = Solution()
nums = [2, 2, 3,1,1,-4,5,-3,0,-7]
#nums = [5,-1,-3,-5,-3]
print So.thirdMax(nums)