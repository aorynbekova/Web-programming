def caught_speeding(speed, is_birthday):
	if is_birthday:
		inc = 5
	else: 
		inc = 0

	if speed <= 60 + inc:
		return 0
	elif 61 <= speed <=80 + inc:
		return 1
	elif speed >= 81 + inc:
		return 2