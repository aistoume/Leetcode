# 763. Partition Labels

class Solution(object):
	def partitionLabels(self, S):
		Lib = {}
		buff = []
		for i in range(len(S)):
			if not S[i] in Lib:
				Lib[S[i]] = i
				buff.append(i)
			else: buff.append(Lib[S[i]])
		for i in range(len(buff)-2,-1,-1):
			buff[i] = min(buff[i],buff[i+1])
		for i in range(1,len(buff)):
			buff[i] = buff[buff[i]]
		s,ans = list(set(buff)),[]
		s.sort()
		while s:
			ans.append(buff.count(s.pop()))
		return ans[::-1]
So = Solution()
S = "dpflgpipdaohuufwcskxcxbbe"
print So.partitionLabels(S)