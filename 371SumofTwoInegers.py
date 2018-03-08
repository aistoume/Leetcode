### Youbin 2017/06/22
### Sum of Two Integers

class Solution(object):
	def getSum(self, a, b):
		if a<0:
			x = ~a
			sum = x^1
			carry = x&1
			while(carry!=0):
				x = sum
				y = carry*2
				sum = x^y
				carry = x&y
			a = x
		if b<0:
			x = ~b
			sum = x^1
			carry = x&1
			while(carry!=0):
				x = sum
				y = carry*2
				sum = x^y
				carry = x&y
			b = x
		sum = a^b
		carry = a&b
		while(carry!=0):
			a = sum
			b = carry*2
			sum = a^b
			carry = a&b
		return sum
		
		
		
	
s = Solution()
a = -1
b = 0
# r = s.getSum(a,b)
x = int(-1)
y = int(1)
sum = x^y
carry = x&y
while carry!=0:
	carry = carry<<1
	buff = sum^carry
	carry = sum^carry
	sum = buff
	print carry,sum
print type(x)
print sum