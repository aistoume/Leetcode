### Youbin 2017/06/20
### 136 Single Number

class Solution(object):
    def singleNumber(self, nums):
		temp = {}
		for i in nums:
			if temp.has_key(i):
				temp[i] = False
			else:
				temp[i] = True
		k = temp.keys()
		v = temp.values()
		return k[v.index(True)]
		
		
s = Solution()
l = [1,1,2,2,3,4,3]
r = s.singleNumber(l)

print r