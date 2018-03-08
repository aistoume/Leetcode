# 455 Assign Cookies
# Youbin Mo 12/21/2017

class Solution(object):
	def findContentChildren(self, g, s):
		count = 0
		g.sort()
		s.sort()
		while s:
			s_max = s.pop()
			while g:
				g_max = g.pop()
				if s_max>=g_max:
					count+=1
					break
		return count
			
				
	
so = Solution()
g = [4,8,9,2,3,3,4,5,6]
s = [1,1,2]

print so.findContentChildren(g,s)