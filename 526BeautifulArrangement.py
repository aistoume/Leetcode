### Youbin 2017/06/25
### 526 Beautiful Arrangement

class Solution(object):
	def countArrangement(self, n):
		count = 0
		count = self.fac(n, [], [False]*n, 0, count)
		return count
	
	def fac(self, n, currList, visitedList, currCount, count):
		if currCount == n:
			count+=1
			return count
		for i in range(n):
			if visitedList[i]==False and ((i+1)%(currCount+1)==0 or (currCount+1)%(i+1)==0):
				visitedList[i] = True
				count = self.fac(n, currList+[i+1], visitedList, currCount+1, count)
				visitedList[i] = False
		return count 
	
def f(n, currList, visitedList, currCount):
	if currCount ==n:
		print currList
		return
	for i in range(n):
		if visitedList[i]==False:
			visitedList[i] = True
			f(n, currList+[i+1], visitedList, currCount+1)
			visitedList[i] = False
		
		
s = Solution()
l = 3
#r = s.countArrangement(l)
l = [1,2,3]
#f(3,[],[False]*3, 0)
r = s.countArrangement(7)
print r