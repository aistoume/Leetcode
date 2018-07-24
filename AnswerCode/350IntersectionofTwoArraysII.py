# 350. Intersection of Two Arrays II


class Solution(object):
	def intersect(self, nums1, nums2):
		ans = []
		if len(nums1)<len(nums2):
			nums1,nums2 = nums2,nums1
		for n in nums1:
			try:
				i = nums2.index(n)
				ans.append(n)
				del nums2[i]				
			except ValueError:
				continue
		return ans
	
So = Solution()
input1 = [1,2,2,1]
input2 = [3,2,2]

print So.intersect(input1,input2)

	