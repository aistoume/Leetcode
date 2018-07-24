class Solution(object):
	def uniqueMorseRepresentations(self, words):
		CodeBook = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]				
		Lib = {}
		for i in range(0,26):
			Lib[chr(i+ord('a'))] = CodeBook[i]
		Collection = []
		for w in words:
			s = [Lib[c] for c in w]
			Collection.append(''.join(s))
		return len(set(Collection))
		
		
S = Solution()
word = ["gin", "zen", "gig", "msg"]
print S.uniqueMorseRepresentations(word)
