def lucky_sum(a,b,c):
	if a == 13:
		return 0
	elif b == 13:
		return a
	elif c == 13:
		return a + b
	return a + b + c


print(lucky_sum((int(input()),int(input()),int(input()))))