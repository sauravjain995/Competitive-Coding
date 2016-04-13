import copy
for _ in range(input()):
	a = input()
	b = map(int,raw_input().split())
	c = copy.copy(b)
	c.reverse()
	sum = 0
	for i in range(a):
		sum += (c[i] - b[i])*(a-i-1)
	print sum