# 118. Pascal's Triangle

class Solution(object):
	def generate(self, numRows):
		ans = [[1],[1,1]]
		if numRows == 0: return []
		elif  numRows<=2: return ans[:numRows]
		i = 2
		while i < numRows:
			ans.append([1]+[ans[i-1][k]+ans[i-1][k+1] for k in range(len(ans[i-1])-1)]+[1])
			i+=1
		return ans

So = Solution()
n = 5
print So.generate(n)