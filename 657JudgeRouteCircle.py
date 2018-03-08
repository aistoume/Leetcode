# Youbin Mo 11/22/2017
# 657 Judge Route Circle

class Solution(object):
	def judgeCircle(self, moves):
		place = [0,0]
		for m in moves:
			if m == 'U':
				place[1]+=1
			if m == 'D':
				place[1]-=1
			if m == 'L':
				place[0]-=1
			if m == 'R':
				place[0]+=1
		return place==[0,0]
				
	
Seq = "UDLLR"
s = Solution()
r = s.judgeCircle(Seq)

print r