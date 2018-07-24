# 859. Buddy Strings

class Solution(object):
	def buddyStrings(self, A, B):
		if not len(A)==len(B): return False
		if not A: return False
		ans = [i for i in range(len(A)) if not A[i]==B[i]]
		if len(ans)==0 and ( len(set(A))==1 or len(set(A))<len(A) ): return True
		if len(ans)==2 and A[ans[0]]==B[ans[1]] and B[ans[0]]==A[ans[1]]:return True
		return False
		
A = "ab"
B = "ab"
So = Solution()
print So.buddyStrings(A,B)