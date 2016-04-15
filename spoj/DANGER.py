import math
while(True):
	a = raw_input()
	if(a=="00e0"):
		break
	else:
		decimal = (10*int(a[0]) + int(a[1])) * 10**(int(a[3]))
		b = pow(2,math.ceil(math.log(decimal,2)))
		c = b-decimal-1
		print int(decimal-c) if c!= -1 else 1