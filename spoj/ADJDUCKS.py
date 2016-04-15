n = input()
a = map(int,raw_input().split())
a.append(1000000007)
a.sort(reverse = True)
a.append(1000000007)
sum = 0
for i in range(1,n+1):
	if ((abs(a[i]-a[i-1]))>=(abs(a[i]-a[i+1]))):
		sum += abs(a[i]-a[i+1])
		a[i] = a[i+1]	
	elif(abs(a[i]-a[i-1])<abs(a[i]-a[i+1])):
		sum += abs(a[i]-a[i-1])
		a[i] = a[i-1]
print sum
