### Youbin 2017/07/13
### 547 Friend Circle


class Solution(object):
	def findCircleNum(self, M):
		n,count = len(M),0
		seen = [False]*n
		for i in range(n):
			stack = []
			if not seen[i]:
				stack.append(i)
				while len(stack):
					curr = stack.pop()
					seen[curr] = True
					for j in range(i+1,n):
						if M[curr][j] and not seen[j]:
							stack.append(j)
							seen[j] = True
				count+=1
				
		return count
			
s = Solution()
l = [[1,1,0],
 [1,1,1],
 [0,1,1]]

r = s.findCircleNum(l)
print r