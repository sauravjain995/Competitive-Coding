import math
a = input()
b = int(math.floor(math.sqrt(a)))
sum = 0
for i in range(1,b+1):
	sum += math.floor(a/i) - (i-1)
print int(sum)
