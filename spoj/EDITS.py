for _ in range(input()):
	A = list(raw_input().strip())
	B = list(raw_input().strip())
	DP = [[0 for x in xrange(3001)] for x in xrange(3001)]
	for i in range(1,len(A)+1):
		DP[0][i] = DP[0][i-1] + 1
	for j in range(1,len(B)+1):
		DP[j][0] = DP[j-1][0] + 1
	for x in range(1,len(B)+1):
		for y in range(1,len(A)+1):
			if A[y-1] == B[x-1]:
				DP[x][y] = DP[x-1][y-1]
			else:
				DP[x][y] = min(DP[x-1][y],DP[x-1][y-1],DP[x][y-1]) + 1
	print DP[len(B)][len(A)]