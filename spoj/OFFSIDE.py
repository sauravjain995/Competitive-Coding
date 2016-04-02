while(True):
	A,D = map(int,raw_input().split())
	if(A == 0 and D== 0):
		break
	else:
		B = map(int,raw_input().split())
		C = map(int,raw_input().split())
		B.sort()
		C.sort()
		if(B[0] < C[1] ):
			print "Y"
		else:
			print "N"
