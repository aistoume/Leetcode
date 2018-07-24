# 796. Rotate String
class Solution(object):
	def rotateString(self, A, B):
		if A == B: return True
		for i in range(len(A)):
			if A[i:] in B and B == (A[i:]+A[0:i]):
				return True
		return False
		
So = Solution()
A = ""
B = ""
print So.rotateString(A,B)