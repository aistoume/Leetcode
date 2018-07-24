# 434. Number of Segments in a String


class Solution(object):
	def countSegments(self, s):
		return len(filter(None, s.split(' ')))
		
So = Solution()
s = "Hello, my name is John"
#s = ""
print So.countSegments(s)

	
	