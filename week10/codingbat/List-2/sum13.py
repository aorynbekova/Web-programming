def sum13(nums):
	tot = 0
	i = 0

	while i < len(nums):
		if nums[i] == 13:
			i += 1
		else:
			tot += nums[i]
		i += 1
	return tot
