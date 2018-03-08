# Counting inversions of a list of distinct integers

def Mergesort(a):
	n = len(a)
	if n>1:
		(ML, c1) = Mergesort(a[:n/2])
		(MR, c2) = Mergesort(a[n/2:])
		L,c = Merge(ML,MR)
		return (L,c1+c2+c)
	else:
		return (a,0)
	
	
def Merge(x,y):
	if len(x)== 0:
		return (y,0)
	if len(y) == 0:
		return (x,0)
	if x[0]<=y[0]:
		L,c = Merge(x[1:],y)
		return [x[0]]+L,c
	else:
		L,c = Merge(x,y[1:])
		return [y[0]]+L,c+len(x)
		
a = [41, 72, 3, 74, 31]
x = [1]
y = [0]
(B,d) = Mergesort(a)
print B
print d