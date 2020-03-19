def no_teen_sum(a,b,c):
	return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
	if 13 <= n <= 19 and n != 15 and n != 16:
	#if 13 <= n <= 19 and n not in [15, 16]:
	#if n in [13, 14, 17, 18, 19]:
		return 0 
	
	return n
print(no_teen_sum((int(input()),int(input()),int(input()))))