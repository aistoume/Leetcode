# 383 Ransom Note
# Youbin Mo 12/21/2017

class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		L = list(magazine)
		for i in ransomNote:
			if i in L:
				L.remove(i)
			else:
				return False
		return True
		
s = Solution()


ransomNote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"
ransomNote = "fffbfgaab"
magazine = "effjfggbffjdgbjjhhdegh"

print s.canConstruct(ransomNote, magazine)