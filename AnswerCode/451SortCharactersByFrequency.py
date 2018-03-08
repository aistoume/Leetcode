### Youbin 2017/07/13
### 451 Sort Characters By Frequency

import operator

class Solution(object):
	def frequencySort(self, s):
		if s == "":
			return ""
		dict = {}
		for i in s:
			if dict.has_key(i):
				dict[i] +=1
			else:
				dict[i] = 1
		dict2 = sorted(dict.items(),key = operator.itemgetter(1))
		dict2.reverse()
		str = "".join(k[0]*k[1] for k in dict2)
		return str
s = Solution()
l = "aafadbaf"
r = s.frequencySort(l)

print r
