for _ in range(input()):
	a = raw_input()
	l = []
	for i in range(len(a)):
		if(a[i] != ')'):
			l.append(a[i])
		else:
			l2 = []
			while(l[-1] != '('):
				l2.append(l.pop())
			l.pop()
			l.append(l2[2] + l2[0] + l2[1])
	print l[0]