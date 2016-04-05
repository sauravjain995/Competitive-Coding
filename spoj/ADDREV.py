def reverse(n):
	a = 0
	while(n>=1):
		a=(a*10) + n%10
		n = n/10
	return a

for _ in range(input()):
	a,b = map(int,raw_input().split())
	print reverse(reverse(a)+reverse(b))