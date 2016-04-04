while(True):
	a=input()
	flag = True
	if(a==0):
		break
	else:
		A = map(int,raw_input().split())
		l=[]
		count = 1
		for i in range (a):
			if(A[i] == count):
				count +=1
				while(len(l)!=0 and l[-1] == count):
					l.pop()
					count += 1
			elif(len(l)!=0 and l[-1] == count):
				l.pop()
				count+=1
			else:
				l.append(A[i])
		if(len(l) == 0):
			print "yes"
		else:
			print "no"

