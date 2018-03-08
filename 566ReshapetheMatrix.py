### Youbin 2017/06/20
### 566 Reshape the Matrix


class Solution(object):
    def matrixReshape(self, nums, r, c):
		row = len(nums)
		col = len(nums[0])
		temp = list()
		M = list()
		if row*col != r*c:
			return nums
		for i in range(0,r*c):
			temp.append(nums[i/col][i%col])
			if len(temp)==c:
				M.append(temp)
				temp = list()
				
		return M
		
		
		

a = [[1,2,3],[4,5,6]]
s = Solution()
r = s.matrixReshape(a, 3, 2)
print r