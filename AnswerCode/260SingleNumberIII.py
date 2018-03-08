### Youbin 2017/07/13
### 260 Single Number III

class Solution(object):
	def singleNumber(self, nums):
		List = []
		for i in nums:
			if i in List:
				List.remove(i)
			else:
				List.append(i)
		return List
		
	
s = Solution()
l = [1,2,1,3,2,5]
r = s.singleNumber(l)

print r