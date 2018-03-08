# 349. Intersection of Two Arrays
# Youbin Mo 12/21/2017

class Solution(object):
	def intersection(self, nums1, nums2):
		return list(set(nums1).intersection(set(nums2)))
		
s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
r = s.intersection(nums1,nums2)
print r

