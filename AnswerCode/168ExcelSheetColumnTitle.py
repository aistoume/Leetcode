# 168 Excel Sheet Column Title
# Youbin Mo 12/18/2017

class Solution(object):
	def convertToTitle(self, n):
		title = ''
		while n >0:
			n-=1
			title = chr(65+n%26)+title
			n = n/26
		return title
		
		
s = Solution()
r = s.convertToTitle(5262)
print r	
		