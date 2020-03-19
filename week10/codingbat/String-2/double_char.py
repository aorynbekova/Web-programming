def double_char(str):
	char = ""
	for ch in str:
		char = char + (ch*2)
	return char

print(double_char(input()))