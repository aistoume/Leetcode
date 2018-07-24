# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
	n = 2
	if num == n: return 0
	elif 1<=num<n: return 1
	else: return -1
	
	
class Solution(object):
	def guessNumber(self, n):
		L,H= 1,n
		while guess(L):
			mid = (L+H+1)/2
			if guess(mid)>=0: L = mid
			else: H = mid
		return L
			
	
So = Solution()
for n in range(2,20):
	print So.guessNumber(n)

