for _ in range(input()):
	a,b,c = map(int,raw_input().split())
	n = (c*2)/(a+b)
	d = (b-a)/(n-5)
	print n
	x = a - (2*d)
	for i in range(1,n+1):
		print x+((i-1)*d),