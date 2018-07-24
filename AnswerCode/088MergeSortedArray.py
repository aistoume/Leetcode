# 88. Merge Sorted Array

class Solution(object):
	def merge(self, nums1, m, nums2, n):
		if n==0: return 
		pt1 = pt2 = count = 0
		while pt1<m+n and count<m and pt2<n:
			if nums1[pt1]>nums2[pt2]:
				nums1[pt1:] = [nums2[pt2]]+nums1[pt1:m+n-1]
				pt2+=1
			else: count+=1
			pt1+=1
		if pt2<n:
			nums1[pt1:] = nums2[pt2:]
		print nums1
			
nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
So = Solution()
So.merge(nums1,m,nums2,n)