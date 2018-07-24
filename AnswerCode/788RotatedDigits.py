# 788 Rotated Digits

class Solution(object):
	def rotatedDigits(self, N):
		count = 0
		for i in range(1,N+1):
			if i != self.flip(i):
				count+=1
				print i
		return count
	def flip(self, n):
		string = str(n)
		num = ""
		for i in string:
			if i =='2':
				num+='5'
			elif i =='5':
				num+='2'
			elif i == '6':
				num+='9'
			elif i =='9':
				num+='6'
			elif i == '3' or i == '7' or i == '4':
				return int(string)
			else:
				num+=i
		return int(num)
	
So = Solution()
print So.rotatedDigits(857)

