### Youbin 2017/07/17
### 347 Top K Frequent Elements

import operator
class Solution(object):
	def topKFrequent(self, nums, k):
		if len(nums)<=1:
			return nums
		dict = {}
		for i in nums:
			if dict.has_key(i):
				dict[i] +=1
			else:
				dict[i] = 1
		dict2 = sorted(dict.items(),key = operator.itemgetter(1))
		dict2.reverse()
		#print dict2[0:k]
		return [n[0] for n in dict2[0:k]]
		
s = Solution()
l = [1,1,1,2,2,3,4]
r = s.topKFrequent(l, 2)

print r