# 686. Repeated String Match

class Solution(object):
	def repeatedStringMatch(self, A, B):
		if not B: return 0
		if not A: return -1
		strs = A
		while len(strs)<=2*len(B) and not B in strs:strs+=A
		if B in strs: return len(strs)/len(A)
		else: return -1
		
So = Solution()
A = "abcd"
B = "abcdabcd"
print So.repeatedStringMatch(A,B)