for _ in range(input()):
	x = raw_input()
	a = input()
	sum = 0
	for i in range(a):
		b = input()
		sum += b
	if(sum % a == 0):
		print "YES"
	else:
		print "NO"