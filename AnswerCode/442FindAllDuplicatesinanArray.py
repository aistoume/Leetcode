### Youbin 2017/06/26
### 442 Find All Duplicates in an Array

class Solution(object):
	def findDuplicates(self, nums):
		List = []
		dic = {}
		for i in nums:
			if dic.has_key(i):
				if dic[i] == 1:
					List.append(i)
			else:
				dic[i] = 1
		List.sort()
		return List

	
s = Solution()
l = [4,3,2,7,8,2,3,1]
r = s.findDuplicates(l)
print r