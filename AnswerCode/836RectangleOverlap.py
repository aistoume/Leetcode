# 836. Rectangle Overlap

class Solution(object):
	def isRectangleOverlap(self, rec1, rec2):
		return not (rec1[0]>=rec2[2] or rec1[2]<=rec2[0] or rec1[1]>=rec2[3] or rec1[3]<=rec2[1])

		
So = Solution()


rec1 = [0,0,1,1]

rec2 = [1,0,2,1]
print So.isRectangleOverlap(rec1,rec2)