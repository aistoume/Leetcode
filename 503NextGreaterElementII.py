### Youbin 2017/07/18
### 503 Next Greater Eletment II

class Solution(object):
	def nextGreaterElements(self, nums):
		stack = []
		Len = len(nums)
		List = [-1]*Len
		if Len<2:
			return List
		for i in range(Len,0,-1):
			while stack != []:
				MAX = stack[-1][0]
				index = stack[-1][1]
				if nums[i-1]>MAX:
					stack.pop()
				elif nums[i-1]<MAX:
					List[i-1] = MAX
					break
				else:
					break
			stack.append((nums[i-1],i))
		for i in range(Len,0,-1):
			while stack != []:
				MAX = stack[-1][0]
				index = stack[-1][1]
				if nums[i-1]>=MAX:
					stack.pop()
				elif nums[i-1]<MAX:
					List[i-1] = MAX
					break			
			stack.append((nums[i-1],i))
		return List
				
			
		
	
s = Solution()
l = [1,2,1]
l = [5,4,3,2,1]
r = s.nextGreaterElements(l)
print r