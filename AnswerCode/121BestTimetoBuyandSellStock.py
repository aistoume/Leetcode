# 121. Best Time to Buy and Sell Stock

class Solution(object):
	def maxProfit(self, prices):
		if len(prices)<2:
			return 0
		maxSell = prices[-1]
		profit = 0
		for p in prices[::-1]:
			profit = max(profit, maxSell-p)
			maxSell = max(maxSell, p)
		return profit
		
		
So = Solution()
input = [7,1,5,3,6,4]
print So.maxProfit(input)