### Youbin 2017/06/24
### 537 Complex Number Multiplication

class Solution(object):
	def complexNumberMultiply(self, a, b):
		x = a.split('+')
		a1 = int(x[0])
		a2 = int(x[1][0:len(x[1])-1])
		y = b.split('+')
		b1 = int(y[0])
		b2 = int(y[1][0:len(y[1])-1])
		real = a1*b1-a2*b2
		image = a1*b2+a2*b1
		r = str(real)+"+"+str(image)+"i"
		return r
	
a = "1+1i"
b = "1+1i"
s = Solution()
r = s.complexNumberMultiply(a,b)
print r