### Youbin 2017/07/13
### 238 Product of Array Except Self

class Solution(object):
	def productExceptSelf(self, nums):
		p,n = 1,len(nums)
		List = []
		for i in range(n):
			List.append(p)
			p*=nums[i]
		p = 1
		for i in range(n-1,-1,-1):
			List[i]*=p
			p*=nums[i]
		return List
		
s = Solution()
l = [1,2,3,4]
r = s.productExceptSelf(l)
print r