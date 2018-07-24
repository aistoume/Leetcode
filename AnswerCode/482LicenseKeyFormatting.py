# 482. License Key Formatting

class Solution(object):
	def licenseKeyFormatting(self, S, K):
		ans = ""
		count = 0
		for c in S[::-1]:
			if not c=='-':
				count+=1
				ans+=c
				if count%K==0: ans+='-'
		if not ans: return ""
		if ans[-1]=='-': return ans[-2::-1].upper()
		return ans[::-1].upper()
		
So = Solution()
S = "---"
K = 3
print So.licenseKeyFormatting(S,K)
