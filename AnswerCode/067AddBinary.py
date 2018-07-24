# 67. Add Binary

class Solution(object):
	def addBinary(self, a, b):
		ans = ""
		carry = 0
		if len(a)<len(b):
			a,b = b,a
		while a and b:
			s = int(a[-1])+int(b[-1])+carry
			ans+= str(s%2)
			carry = s/2
			a = a[:-1]
			b = b[:-1]	
		while a:
			s = int(a[-1])+carry
			ans+= str(s%2)
			carry = s/2
			a = a[:-1]
		if carry:
			ans+=str(carry)
		return ans[::-1]
So = Solution()
a = "1010"
b = "1011"
print So.addBinary(a,b)