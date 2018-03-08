### Youbin 2017/06/23
### 599 Minimum Index Sum of Two List


class Solution(object):
	def findRestaurant(self, list1, list2):
		dic = {}
		M = 9999
		if len(list1)<len(list2):
			L1 = list1
			L2 = list2
		else:
			L1 = list2
			L2 = list1
		for name in L1:
			if name in L2>=0:
				s = L1.index(name)+L2.index(name)
				dic[name] = s
				M = min(s,M)
		v = dic.values()
		k = dic.keys()
		L = []
		for i in range(len(v)):
			if v[i]==M:
				L.append(k[i])
		return L
	
s = Solution()
l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
l2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

r = s.findRestaurant(l1,l2)
print r
