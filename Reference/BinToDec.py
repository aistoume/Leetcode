# Binary to Decimal

def BinToDec(b):
	n = len(b)
	if n == 0:
		return (0,1)
	if n == 1:
		return (b[0],1)
		
	SL,factor1 = BinToDec(b[:n/2])
	SR,factor2 = BinToDec(b[n/2:])
	factor = factor2*2
	SL = factor*SL
	s = SL+SR
	print b
	print "s=",s,factor
	return s,factor*factor1




b = [1,0,1,1,0,1,1,0,1,1,0]
d,f = BinToDec(b)
print d