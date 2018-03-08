### Youbin 2017/06/23
### 492 Construct the Rectangle

class Solution(object):
	def constructRectangle(self, area):
		w = int(area**0.5)
		while area%w!=0:
			w -=1
		return ([area/w, w])
		
s = Solution()
area = 10
r = s.constructRectangle(area)

print r