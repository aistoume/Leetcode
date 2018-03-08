# 744 Find Smallest Letter Greater Than Target
# Youbin Mo 12/11/2017

class Solution(object):
	def nextGreatestLetter(self, letters, target):
		m = 200
		t = ord(target)
		for k in letters:
			curr = ord(k)
			if curr<= t:
				curr+=26
			if curr<m:
				m = curr
		if m>122:
			m-=26
		return chr(m)
		
		
s = Solution()
l = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

r = s.nextGreatestLetter(l,"z")
print r
