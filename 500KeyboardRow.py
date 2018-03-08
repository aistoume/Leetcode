### Youbin 2017/06/20
### 500 Keyboard Row

class Solution(object):
    def findWords(self, words):
		List = []
		dic = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]
		
		for i in range(len(words)):
			w = words[i]
			flag = 1
			for j in range(3):
				if dic[j].find(w[0]) >= 0:
					row = j
			for j in range(1,len(w)):
				if dic[row].find(w[j]) < 0:
					flag = 0
					break
			if flag:
				List.append(w)
		return List
		
		
s = Solution()
l = ["Hello", "Alaska", "Dad", "Peace"]
r = s.findWords(l)
a = "qwertyuiop"
print r