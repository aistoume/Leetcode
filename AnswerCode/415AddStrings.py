# 415. Add Strings

class Solution(object):
    def addStrings(self, num1, num2):
		ans = ""
		carry = 0
		if len(num1)<len(num2):
			num1,num2 = num2,num1
		while num1 and num2:
			s = int(num1[-1])+int(num2[-1])+carry
			ans+= str(s%10)
			carry = s/10
			num1 = num1[:-1]
			num2 = num2[:-1]	
		while num1:
			s = int(num1[-1])+carry
			ans+= str(s%10)
			carry = s/10
			num1 = num1[:-1]
		if carry:
			ans+=str(carry)
		return ans[::-1]
	
	
So = Solution()
num1 = "1"
num2 = "9"
print So.addStrings(num1,num2)