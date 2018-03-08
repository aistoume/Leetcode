# 717 1-bit and 2-bit Characters
# Youbin Mo

class Solution(object):
	def isOneBitCharacter(self, bits):
		n = len(bits)
		if n == 1:
			if bits[0]== 0:
				return True 
			else: return False
		if n==2 and bits[0]== 1:
			return False
		if bits[0] ==0:
			return self.isOneBitCharacter(bits[1:])
		else:
			return self.isOneBitCharacter(bits[2:])
		
s = Solution()
b = [1,1,1,0]
r = s.isOneBitCharacter(b)
print r