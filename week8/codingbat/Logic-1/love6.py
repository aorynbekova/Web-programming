def love6(a, b):
	tot = a + b
	diff = abs(a-b)

	if a == 6 or b == 6:
		return True
	return tot == 6 or diff == 6