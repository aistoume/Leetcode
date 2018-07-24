row,col = len(A),len(A[0])
		for k in range(row):
			A[k] = ([i if A[k][0] else int(not i) for i in A[k]])