### Youbin 2017/06/20
### 476 Number Complement

class Solution(object):
	def findComplement(self, num):
		"""
		:type num :int
		:rtype: int
		"""
		b = 0
		a = bin(num)
		k = 0
		for i in range(len(a)-1,1,-1):
			if (a[i] == '0'):
				b+=2**k
			k+=1
			#print a[i]
		return b