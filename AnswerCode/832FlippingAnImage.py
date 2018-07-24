class Solution(object):
	def flipAndInvertImage(self, A):
		M =[]
		for L in A:
			M.append([int(not L[i]) for i in range(len(L)-1,-1,-1)])
		return M
	
	
	
S = Solution()
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print S.flipAndInvertImage(A)