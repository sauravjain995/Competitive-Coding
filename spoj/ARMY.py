for _ in range(input()):
	blank = raw_input()
	NG, NM = map(int,raw_input().split())
	A = map(int,raw_input().split())
	B = map(int,raw_input().split())
	x = max(A)
	y = max(B)
	if(x >= y ):
		print "Godzilla"
	else:
		print "MechaGodzilla"