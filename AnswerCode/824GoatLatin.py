#824. Goat Latin

class Solution(object):
	def toGoatLatin(self, S):
		st = S.split(' ')
		re = []
		v = ['a','e','i','o','u','A','E','I','O','U']
		for w in st:
			if w[0] in v:
				re.append(w+"ma"+'a'*(len(re)+1))
			else:
				re.append(w[1:]+w[0]+"ma"+'a'*(len(re)+1))
		re = ' '.join(re)
		return re
	
So = Solution()
st = "The quick brown fox jumped over the lazy dog"
print So.toGoatLatin(st)