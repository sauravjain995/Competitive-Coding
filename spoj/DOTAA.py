import math
for _ in range(input()):
	n,m,D = map(int,raw_input().split())
	for i in range(n):
		a = input()
		a = math.ceil(a/D)
		m -= a-1
	if(m<=0):
		print "YES"
	else:
		print "NO"

