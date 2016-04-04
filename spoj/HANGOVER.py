while(True):
	a = raw_input()
	if(a=="0.00"):
		break
	else:
		b = float(a)
		i = 2
		sum = 0
		count = 0
		while (sum < b):
			sum += 1.0/i
			i += 1
			count += 1
	print count,"card(s)"