import sys
for _ in range(input()):
	a = input()
	count = 0
	count1=0
	for i in range(1,10000):
		sum=0
		sum+=(i*(i+1))/2
		if(sum<a):
			count1 = a-sum
			count += 1
		else:
			break
	d = count+2-count1
	if(count % 2 == 0):
		print "TERM",a,"IS",str(d),
		sys.stdout.write("/"),
		print str(count+2-d)
	else:
		print "TERM",a,"IS",str(count+2-d),
		sys.stdout.write("/"),
		print str(d)
