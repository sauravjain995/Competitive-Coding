for _ in range(input()):
	a = input()
	if(a==0):
		print "0"
	else:
		print ((2*a) + ((a*a)-1) + ((a-1)*(a-2))/2)%1000007
