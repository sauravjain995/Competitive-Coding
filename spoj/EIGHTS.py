for _ in range(input()):
	a = input()
	l= [192,442,692,942]
	if a in range(5):
		print l[a-1]
	else:
		print (str((a-1)/4) + str(l[(a-1)%4]) )