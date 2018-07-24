# 345. Reverse Vowels of a String

class Solution(object):
	def reverseVowels(self, s):
		vow = "aeiouAEIOU"
		s = list(s)
		i,j = 0,len(s)-1
		while i<j:
			while i<len(s)-1 and not s[i] in vow:
				i+=1
			while j>0 and not s[j] in vow:
				j-=1
			if i<j:
				s[i],s[j] = s[j],s[i]
			i+=1
			j-=1
		return "".join(s)
			
		
So = Solution()
s = "hello"
s=".j"
print So.reverseVowels(s)