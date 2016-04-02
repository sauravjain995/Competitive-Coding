def findsum(a):
	sum = 0
	for i in range(len(a)):
		sum += a[i]*a[i]
	return sum
a = list(map(int,raw_input().strip()))
l=[]
#print a
count = 0
while(sum != 1 or sum not in l):
	sum = findsum(a)
	#print sum
	count += 1
	if(sum == 1 ):
		print count
		break
	if(sum!=1 and sum in l):
		print "-1"
		break
	if(sum!=1 and sum not in l):
		l.append(sum)
	a=map(int,str(sum).strip())
	#print a

