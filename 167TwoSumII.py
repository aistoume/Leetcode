### Youbin 2017/06/23
### Two Sum II - Input array is sorted

class Solution(object):
	def twoSum(self, numbers, target):
		dic = {}
		for i in range(len(numbers)):
			curr = numbers[i]
			if dic.has_key(curr):
				dic[curr].append(i)
			else:
				dic[curr] = [i]
		v = dic.values()
		k = dic.keys()
		k.sort()
		print k
		for i in k:
			if (target-i) in k:
				x = dic[i][0]
				y = dic[target-i][0]
				if x == y:
					y+=1
				return [x+1,y+1]
		return []
s = Solution()
l = [-1,0]
r = s.twoSum(l,-1)
print r