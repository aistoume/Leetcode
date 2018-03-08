### Youbin 2017/06/22
### 448 Find All Numbers Disappeared in an Array

class Solution(object):
	def findDisappearedNumbers(self, nums):
		r = [0]*len(nums)
		for i in nums:
			r[i-1] = 1
		temp = []
		count =1
		for i in range(len(nums)):
			p = count*r[i]
			if p==0:
				temp.append(count)
			count+=1
		return temp

s = Solution()		
l = [4,3,2,7,8,2,3,1]
r = s.findDisappearedNumbers(l)
print r