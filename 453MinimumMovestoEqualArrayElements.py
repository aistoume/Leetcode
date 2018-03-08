# 453 Minimum Moves to Equal Array Elements
# Youbin Mo 12/18/2017

class Solution(object):
	def minMoves(self, nums):
		m = min(nums)
		moves = 0
		for i in nums:
			moves+= i -m
		return moves
	
s = Solution()
L = [1,2,3,2]
r = s.minMoves(L)
print r