# 70. Climbing Stairs

class Solution(object):
	def climbStairs(self, n):
		L = [1,1]
		while len(L)<=n:
			L.append(L[-1]+L[-2])
		return L[-1]
	
So = Solution()
n = 4
print So.climbStairs(n)