import copy
for _ in range(input()):
	z = raw_input()
	a = raw_input().split()
	b = copy.copy(a)
	for i in range(len(a)):
		if 'machula' in a[i]:
			x = i
			a.remove(a[i])
			break
	for i in a:
		if i == '=':
			a.remove(i)
	if a[0] == "+":
		c = int(a[2]) - int(a[1])
		print str(c) + " " + a[0] + " " + a[1] + " " +  "=" + " " + a[2]
	if(a[1] == "+" and x == 2):
		c = int(a[2]) - int(a[0])
		print a[0] + " " + a[1] + " " + str(c) + " " + "=" + " " + a[2]
	if(a[1] == "+" and x == 4):
		c = int(a[0]) + int(a[2])
		print a[0] + " " + a[1] + " " + a[2] + " " + "=" + " " + str(c)