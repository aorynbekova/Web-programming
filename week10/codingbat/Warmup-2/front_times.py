def front_times(str, n):
    if len(str) < 3:
        return str * 3
    return str[:3] * n
print(front_times(input(), int(input())))