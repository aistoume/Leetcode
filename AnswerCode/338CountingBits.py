### Youbin 2017/06/24
### 338 Counting Bits

class Solution(object):
	def countBits(self, num):
		curr = 0
		next = 1
		List = [0]
		for i in range(1,num+1):
			List.append(List[curr]+1)
			curr+=1
			if curr == next:
				next = 2*curr
				curr = 0
		return List

a = 10
s = Solution()
r = s.countBits(a)
print r