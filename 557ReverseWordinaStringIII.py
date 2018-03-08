### Youbin 2017/06/20
### 557 Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
		temp = []
		s = s.split(' ')
		for i in range(len(s)):
			a = s[i]
			a = a[::-1]
			temp.append(a)
			if i < len(s)-1:
				temp.append(' ')
		temp = ''.join(temp)
		return temp
		
s = Solution()
st = s.reverseWords('string')
print st