for _ in range(input()):
	a,b = map(int,raw_input().split())
	if(b!=a and a!= b+2):
		print "No Number"
	else:
		if(a%2==1 and b%2==1):
			print a+b-1
		else:
			print a+b