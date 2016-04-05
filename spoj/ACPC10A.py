while (True):
	a,b,c = map(int,raw_input().split())
	if(a==b==c==0):
		break
	else:
		if(c-b == b-a):
			print "AP",
			print (c+ (b-a))
		else:
			print "GP",
			print (c*(b/a))