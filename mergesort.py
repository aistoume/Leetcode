# Mergesort 1 array

def Merge(x,y):
	if len(x) == 0:
		return y
	if len(y) == 0:
		return x
	if x[0]<=y[0]:
		return [x[0]]+Merge(x[1:],y)
	else:
		return [y[0]]+Merge(x,y[1:])
		
def Mergesort(a):
	n = len(a)
	if n>1:
		ML = Mergesort(a[0:n/2])
		MR = Mergesort(a[n/2:])
		return Merge(ML,MR)
		
	else:
		return a



a = [41,15,897,132,1,5,67,54,12,0,6,8]
b = Mergesort(a)
print b