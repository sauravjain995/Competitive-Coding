for _ in range(input()):
	a = input()
	A=raw_input()
	B = list(A)
	ttt = tth = tht = thh = htt = hth = hht = hhh = 0
	for i in range(len(B)-2):
		if(B[i] + B[i+1]+B[i+2] == "TTT"):
			ttt += 1
		if(B[i] + B[i+1]+B[i+2] == "TTH"):
			tth += 1
		if(B[i] + B[i+1]+B[i+2] == "THT"):
			tht += 1
		if(B[i] + B[i+1]+B[i+2] == "THH"):
			thh += 1
		if(B[i] + B[i+1]+B[i+2] == "HTT"):
			htt += 1
		if(B[i] + B[i+1]+B[i+2] == "HTH"):
			hth += 1
		if(B[i] + B[i+1]+B[i+2] == "HHT"):
			hht += 1
		if(B[i] + B[i+1]+B[i+2] == "HHH"):
			hhh += 1
	print a,ttt,tth,tht,thh,htt,hth,hht,hhh