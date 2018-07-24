# 66. Plus One

class Solution(object):
	def plusOne(self, digits):
		carry=0
		digits[-1]+=1
		ans = []
		for i in digits[::-1]:
			ans.append((i+carry)%10)
			carry=(i+carry)/10
		if carry: ans+=[1]
		return ans[::-1]
		
So = Solution()
digits = [9]
print So.plusOne(digits)