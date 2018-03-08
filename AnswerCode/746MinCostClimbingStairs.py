# 746 Min Cost Climbing Stairs
# Youbin Mo 12/18/2017

class Solution(object):
	def minCostClimbingStairs(self, cost):
		INF = 10**9
		N = len(cost)
		CostArray = [None]*(N+2)
		CostArray[N] = 0
		CostArray[N+1]=0
		N-=1
		while N>=0:
			CostArray[N] = cost[N]+min(CostArray[N+1],CostArray[N+2])
			N-=1
		return min(CostArray[0], CostArray[1])
		
	
	
s = Solution()
cost = [10,15,20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
r = s.minCostClimbingStairs(cost)
print r
	