### Youbin 2017/06/23
### 283 Move Zeros

class Solution(object):
	def moveZeroes(self, nums):
		i = 0
		count =0
		while i<len(nums):
			if nums[i] ==0:
				nums.remove(0)
				count+=1
			else:
				i+=1
		while count>0:
			nums.append(0)
			count-=1
		
s = Solution()
l = [0,1,0,3,12]
s.moveZeroes(l)

print l