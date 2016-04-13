import math 
for _ in range(input()):
	E,N = map(int,raw_input().split())
	if(E==0 or N==0):
		print "0"
	else:
		if(max(E,N)/2 < min(E,N)):
			print (E+N)/3
		else:
			print min(E,N)
	

