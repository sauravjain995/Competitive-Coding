l = []
r=[]
for i in range(input()):
	a = map(int,raw_input().split())
	if a[0] not in r:
		r.append(a[0])
	for j in range(2,2+a[1]):
		if a[j] not in l:
			l.append(a[j])
print len(list(set(l)-set(r)))
		

