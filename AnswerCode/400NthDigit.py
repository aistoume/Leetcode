# 400. Nth Digit

class Solution(object):
	def findNthDigit(self, n):
		digit = maxN = 0
		while n>maxN:
			digit+=1
			maxN+=(10**digit-10**(digit-1))*digit
		index = n - (maxN-(10**digit-10**(digit-1))*digit)-1
		k = 10**(digit-1)+ index/digit
		ans = str(k)[(index)%digit]
		return int(ans)
		
So = Solution()
n = 198
print So.findNthDigit(n)