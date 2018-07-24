# 551. Student Attendance Record I

class Solution(object):
	def checkRecord(self, s):
		if s.count('A')>1:
			return False
		s = s.replace('A','P').split('P')
		for c in s:
			if len(c)>2:
				return False
		return True

So = Solution()
input = "PPALLL"
#input = "PLPALLP"
print So.checkRecord(input)

	