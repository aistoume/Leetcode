# Test Yield function

def yield_test(n):
	print("Start")
	yield n*10
	print("Check point")
	for i in range(n):
		yield call(i)
		print("i=", i)
		
	print("do any other.")
	print("END")
	
def call(i):
	return i*2

for i in yield_test(5):
	print("return value = ", i)