### Youbin 2017/07/25
### 592 Fraction Addition and Subtraction

class Solution(object):
	def fractionAddition(self, expression):
		List = []
		num = ""
		k = 0
		if expression[0] == '-':
			num+='-'
			k=1
		for s in expression[k:len(expression)]:
			if s == '-' or s == '+':
				List.append(num)
				num=s
			else:
				num+=s
		List.append(num)
		while len(List)>1:
			num1 = List.pop()
			num2 = List.pop()
			List.append(self.add2Items(num1,num2))
		return List[0]
	def add2Items(self,num1,num2):
		num1 = num1.split('/')
		num2 = num2.split('/')
		print num1,num2
		numer1,denom1 = int(num1[0]),int(num1[1])
		numer2,denom2 = int(num2[0]),int(num2[1])
		numer = numer1*denom2+numer2*denom1
		denom = denom1*denom2
		if numer==0:
			return "0/1"
		m = min(abs(numer),denom)
		for i in range(m,0,-1):
			if numer%i==0 and denom%i==0:
				break
		return str(numer/i)+'/'+str(denom/i)
		
l = "1/3-1/2"
r = Solution().fractionAddition(l)
print r
