# 122 Best Time to Buy and Sell Stock II
# Youbin Mo 12/18/2017

class Solution(object):
	def maxProfit(self, prices):
		N = len(prices)
		ProfitArray = [[0,0]]*(N+1)

		while N >0:
			N-=1
			ProfitArray[N][0] = ProfitArray[N+1][0]
			if ProfitArray[N+1][1]-prices[N]>ProfitArray[N][0]:
				ProfitArray[N][0] = ProfitArray[N+1][1]-prices[N]
			ProfitArray[N][1] = ProfitArray[N+1][1]
			if ProfitArray[N+1][0]+prices[N]> ProfitArray[N][1]:
				ProfitArray[N][1] = ProfitArray[N+1][0]+prices[N]
		return ProfitArray[0][0]
				
	
	
s = Solution()
p = [1,10,3,4,5,8,10,31,4]
#p = [1]
r = s.maxProfit(p)
print r