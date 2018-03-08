### Youbin 2017/07/28
### 477 Total Hamming Distance

class Solution(object):
	def totalHammingDistance(self, nums):
		List = [[0]*32,[0]*32]
		for i in nums:
			for k in range(32):
				List[i&1][k]+=1
				i = i>>1

		sum = 0
		for k in range(32):
			sum+= List[0][k]*List[1][k]
		return sum

	

l = [4,12,2]
obj = Solution()
r = obj.totalHammingDistance(l)
print r