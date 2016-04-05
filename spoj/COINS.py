def part(n):
	if(n/4 + n/3 + n/2) < n:
		return n
	else:
		return part(n/4) + part(n/3) + part(n/2)
while(True):
	try:
		b=input()
		print part(b)
	except:
		break
