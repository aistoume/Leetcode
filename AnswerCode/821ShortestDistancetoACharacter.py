# 821. Shortest Distance to a Character
class Solution(object):
    def shortestToChar(self, S, C):
		pt = -99999
		dist = []
		for i in range(len(S)):
			if S[i] == C:
				pt = i
			dist.append(i-pt)
			
		for i in range(pt,-1,-1):
			if S[i] == C:
				pt = i
			dist[i] = min(pt-i, dist[i])
		return dist
				
			
		
S = "loveleetcode"
C = 'e'
So = Solution()

print So.shortestToChar(S,C)