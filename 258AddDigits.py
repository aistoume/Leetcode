### Youbin 2017/06/23
### 258 Add Digits

class Solution(object):
	def addDigits(self, num):
		while num > 9:
			res = num%10
			num = (num/10)+res
		return num
	
	def addDigits2(self, num):
    """
    :type num: int
    :rtype: int
    """
		if num == 0 : return 0
		else:return (num - 1) % 9 + 1
	
l = 38
s = Solution()
r = s.addDigits(l)
print r