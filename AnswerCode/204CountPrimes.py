# 204. Count Primes

class Solution(object):
	def countPrimes(self, n):
		if n<3: return 0
		ans = [True]*n
		ans[0] = ans[1] = False
		for i in range(2,int(n**0.5)+1):
			if ans[i]:
				ans[i*i: n : i] = [False]*len(ans[i*i: n : i])
		return sum(ans)
	
So = Solution()
n = 10
print So.countPrimes(n)
