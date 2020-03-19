def centered_average(nums):
	small = min(nums)
	large = max(nums)
	nums.remove(small)
	nums.remove(large)

	return int(sum(nums) / len(nums))

