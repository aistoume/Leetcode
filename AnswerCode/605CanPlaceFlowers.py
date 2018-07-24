# 605. Can Place Flowers

class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):
		flowerbed.append(0)
		if not (flowerbed[0] or flowerbed[1]):
			flowerbed[0]=1
			n-=1
		for i in range(1,len(flowerbed)-1):
			if n<=0:return True
			if not (flowerbed[i-1] or flowerbed[i+1] or flowerbed[i]): 
				flowerbed[i]=1
				n-=1
		return n<=0
So = Solution()
flowerbed = [1,0,0,0,1,0,1]
n = 2
print So.canPlaceFlowers(flowerbed,n)