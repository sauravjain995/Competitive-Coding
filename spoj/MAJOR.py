for _ in range(input()):
	n = input()
	A = map(int,raw_input().split())
	l=[]
	d={}
	flag = True
	for i in range(n):
		if A[i] not in d:
			d[A[i]] = 1
		else:
			d[A[i]] += 1
		if(d[A[i]]>n/2):
			flag = False
			k = A[i]
			break
	if(flag == False):
		print "YES",
		print k
	else:
		print "NO"

