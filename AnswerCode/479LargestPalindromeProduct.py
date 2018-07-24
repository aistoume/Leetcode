# 479. Largest Palindrome Product

class Solution(object):
	def largestPalindrome(self, n):
		if n == 1: return 9
		st = 10**n-1
		lowB = st**2
		while st>=10**(n-1):
			pal = int( str(st)+str(st)[::-1])
			st-=1
			root = int(pal**0.5)-1
			if pal>lowB: continue
			for i in range(root,10**n):
				if not pal%i and len(str(pal/i))==n: return pal%1337
			
		
So = Solution()
n = 7
print So.largestPalindrome(n)
