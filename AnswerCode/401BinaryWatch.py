# 401. Binary Watch

class Solution(object):
	def readBinaryWatch(self, num):
		ans = []
		for h in range(12):
			for m in range(60):
				if num==(bin(m)[2:]).count('1')+(bin(h)[2:]).count('1'):
					M = "%02d" %m
					H = "%d" %h
					ans.append(H+":"+M)	
		return ans

				
				
So = Solution()
n = 3
print So.readBinaryWatch(n)