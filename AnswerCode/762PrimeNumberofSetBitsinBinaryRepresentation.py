# 762 Prime Number of Set Bits in Binary Representation

class Solution(object):
	def countPrimeSetBits(self, L, R):
		count = 0
		primeLib = [2,3,5,7,11,13,17,19]
		for i in range(L,R+1):
			b = (list(bin(i)))[2:]
			if b.count('1') in primeLib:
				count+=1
		return count
	

S = Solution()
L = 10
R = 15

print S.countPrimeSetBits(L,R)


