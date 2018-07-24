# 278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	n = 5
	return version>n

class Solution(object):
	def firstBadVersion(self, n):
		if isBadVersion(1):return 1
		lowB,highB = 1,n
		guess = (lowB+highB)/2
		while not highB==lowB:
			guess = (lowB+highB)/2
			if isBadVersion(guess): highB = guess
			else: lowB = guess
			if highB-lowB==1:return highB
		return guess
		
		
		
So = Solution()
n = 10
print So.firstBadVersion(n)