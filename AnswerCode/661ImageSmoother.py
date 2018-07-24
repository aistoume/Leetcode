# 661. Image Smoother

class Solution(object):
	def imageSmoother(self, M):
		ans = [[i for i in a] for a in M]
		neigh = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
		for i in range(len(M)):
			for j in range(len(M[0])):
				count = 1
				for r,c in neigh:
					if 0<=i+r<len(M) and 0<=j+c<len(M[0]):
						ans[i][j]+=M[i+r][j+c]
						count+=1
				ans[i][j]=ans[i][j]/count
		return ans
		
So = Solution()
input = [[1,1,1],[1,0,1],[1,1,1]]

print So.imageSmoother(input)
	
	