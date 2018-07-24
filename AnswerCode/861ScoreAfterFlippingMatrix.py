# 861. Score After Flipping Matrix

class Solution(object):
	def matrixScore(self, A):
		if not A: return 0
		row,col = len(A),len(A[0])
		for k in range(row):
			A[k] = ([i if A[k][0] else int(not i) for i in A[k]])
		base = (1<<(col-1))
		ans = row*base
		for k in range(1,col):
			s = sum([A[i][k] for i in range(row)])
			base = base>>1
			ans+=max(s,row-s)*base
		return ans
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
So = Solution()
print So.matrixScore(A)