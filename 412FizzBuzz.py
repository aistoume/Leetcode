### Youbin 2017/06/20
### 412 Fizz Buzz

class Solution(object):
    def fizzBuzz(self, n):
		List = []
		for i in range(1,n+1):
			if ((i%3 == 0) & (i%5 ==0)):
				List.append("FizzBuzz")
				print i
			elif (i%3 == 0):
				List.append("Fizz")
			elif (i%5 == 0):
				List.append("Buzz")
			else:
				List.append(str(i))	
		return List
s = Solution()
l = 15
r = s.fizzBuzz(l)
print r

print (3==3 & 1==1)