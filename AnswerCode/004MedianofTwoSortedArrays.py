#004 Median of Two Sorted Arrays
# Youbin Mo 12/19/2017

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		if len(nums1)==0:
			L = nums2
		if len(nums2)==0:
			L = nums1
		
		def findMid(self, L):
			N =len(L)
			if N%2==1:
				m = L[(N-1)/2]
			else:
				m = (L[N/2]+L[N/2-1])/2.0
			return m
		if nums1[-1]<nums2[0]:
			L = nums1+nums2
		if nums2[-1]<nums1[0]:
			L = nums2+nums1
		
		
		
		
s = Solution()
nums1 = [1,3,5,7,9]
nums2 = [2,4,6,8,10]

r = s.findMedianSortedArrays(nums1,nums2)
print r