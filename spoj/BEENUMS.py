while(True):
	a=input()
	flag = False
	if(a==-1):
		break
	else:
		i=1
		sum=1
		while(True):
			sum += 6*(i-1)
			i+=1
			if(sum == a):
				print "Y"
				break
			elif(sum > a):
				flag = True
				break
		if(flag == True):
			print "N"