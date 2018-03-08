### Youbin 2017/06/20
### 496 Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
		List = []
		for i in findNums:
			j = nums.index(i)
			flag = 0
			for k in range(j+1,len(nums)):
				if nums[k] > nums[j]:
					List.append(nums[k])
					flag = 1
					break
			if flag==0:
				List.append(-1)
		return List
		
s = Solution()
L1 = [2,4]
L2 = [1,2,3,4]
r = s.nextGreaterElement(L1,L2)

print r