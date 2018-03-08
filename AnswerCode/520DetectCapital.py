### Youbin 2017/06/22
### 520 Detect Capital

class Solution(object):
	def detectCapitalUse(self, word):
		if len(word)<2:
			return True
		dic = "abcdefghijklmnopqrstuvwxyz"
		DIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		if word[0] in dic:
			cap = False
		else:
			cap = True
		
		if not cap:
			flag = True
			for i in word[1:]:
				if not(i in dic):
					return False
			return flag
		else:
			flag = word[1] in dic
			for i in word[2:]:
				if flag^(i in dic):
					return False
			return True


	
s = Solution()
l = "USA"
l = "FlaG"
r = s.detectCapitalUse(l)
print r