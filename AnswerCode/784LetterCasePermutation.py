# 784. Letter Case Permutation
class Solution(object):
    def letterCasePermutation(self, S):
		if S =="":
			return [""]
		if S[0] in "0123456789":
			if len(S)>1:
				return [S[0]+res for res in self.letterCasePermutation(S[1:])]
			else:
				return [S[0]]
		if len(S)==1:
			return [S.lower(), S.upper()]
		return [S[0].lower()+res for res in self.letterCasePermutation(S[1:])]+[S[0].upper()+res for res in self.letterCasePermutation(S[1:])]

So = Solution()
S = ""
print So.letterCasePermutation(S)
