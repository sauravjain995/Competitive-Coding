for _ in range(input()):
	a = input()
	A = map(int,raw_input().split())
	B = map(int,raw_input().split())
	A.sort()
	B.sort()
	sum = 0
	for i in range(a):
		sum += A[i]*B[i]
	print sum