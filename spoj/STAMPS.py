import sys
for j in range(input()):
	R,F = map(int,raw_input().split())
	A = map(int,raw_input().split())
	A.sort(reverse = True)
	sum = 0
	for i in range(F):
		sum += A[i]
		if(sum>=R):
			print "Scenario ",
			sys.stdout.write("#"),
			sys.stdout.write(str(j+1)),
			print (":")
			print i+1
			print
			break
	if(sum<R):
		print "Scenario ",
		sys.stdout.write("#"),
		sys.stdout.write(str(j+1)),
		print (":")
		print "impossible"
		print