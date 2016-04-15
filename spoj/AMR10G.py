for _ in range(input()):
	N,K = map(int,raw_input().split())
	a = map(int,raw_input().split())
	a.sort()
	if(K==1):
		print "0"
	else:
		mini = 1000000007
		for i in range(K-1,N):
			if(a[i]-a[i-K+1]< mini): 
				mini = a[i]-a[i-K+1]
		print abs(mini)
