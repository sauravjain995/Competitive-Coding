while(True):
	N = input()
	if(N== -1):
		break
	else:
		l = []
		for i in range(N):
			l.append(input())
		sum = 0
		count = 0
		for i in l:
			sum += i
		if(sum % N != 0):
			print "-1"
		else:
			a = sum/N
			for i in l:
				if(i<a):
					count += abs(a-i)
			print count
