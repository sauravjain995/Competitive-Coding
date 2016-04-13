from __future__ import division
import math
while(True):
	a=input()
	if(a==0):
		break
	else:
		x = round((a*a)/(2*3.1415926),2)
		print format(x,'.2f')