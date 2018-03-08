# Merge 2 array

def Merge(x,y):
	if len(x) == 0:
		return y
	if len(y) == 0:
		return x
	if x[0]<=y[0]:
		return [x[0]]+Merge(x[1:],y)
	else:
		return [y[0]]+Merge(x,y[1:])





a = [2, 3,4,5,9]
b = [1,3,6,7,10]
x = [1]
y = [0]
c = Merge(x,y)
print c