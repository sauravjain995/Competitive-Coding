from __future__ import division
import math
while(True):
	G,B = map(int,raw_input().split())
	if(G == B == -1):
		break
	a = min(G,B)
	b = max(G,B)
	print int(math.ceil(b/(a+1)))