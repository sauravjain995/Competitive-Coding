while(True):
	a=input()
	if(a==0):
		break
	else:
		sum = 0
		for i in range(1,a+1):
			sum +=  i*i
	print sum