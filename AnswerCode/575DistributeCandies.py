### Youbin 2017/06/20
### 575 Distribute Candies

class Solution(object):
    def distributeCandies(self, candies):
		dic = {}
		for i in range(len(candies)):
			if dic.has_key(candies[i]):
				dic[candies[i]] += 1
			else:
				dic[candies[i]] = 1
		
		return min(len(candies)/2, len(dic.keys()))
		
s = Solution()
l = [1,1,2,3,2,3]
r = s.distributeCandies(l)

print r

a = {}
a[5] = 1
print a.keys()
print a.values()