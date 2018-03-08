### Youbin 2014/06/30
### 540 Single Element in a Sorted Array

class Solution(object):
	def singleNonDuplicate(self, nums):
		l = nums
		x = len(l)
		while x>1:
			mid = (x-1)/2
			if (l[mid]!=l[mid+1] and l[mid]!=l[mid-1]):
				return l[mid]
			if mid%2 == 0:
				if l[mid]==l[mid-1]:
					l = l[0:mid+1]
					x = len(l)
				elif l[mid]==l[mid+1]:
					l = l[mid:x]
					x = len(l)
			elif mid%2 == 1:
				if l[mid]==l[mid-1]:
					l = l[mid+1:x]
					x = len(l)
				elif l[mid]==l[mid+1]:
					l = l[0:mid]
					x = len(l)
		return l[0]
	
s = Solution()
l = [1,1,2,3,3,4,4,8,8]
l = [3,3,7,7,10,11,11]
r = s.singleNonDuplicate(l)
print r