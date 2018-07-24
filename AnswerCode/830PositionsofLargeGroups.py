# 830. Positions of Large Groups

class Solution(object):
	def largeGroupPositions(self, S):
		ans = []
		start = 0
		end = 0
		cs = S[0]
		S+=';'
		for i in range(1,len(S)):
			if not S[i] == cs:
				if i-1-start>1:
					ans.append([start,i-1])
				start = i
				cs = S[i]
		return ans
	
input = "abcdddeeeeaabbbcd"  # Output = [[3,5],[6,9],[12,14]]
input = "aaa"
So = Solution()
print So.largeGroupPositions(input)


