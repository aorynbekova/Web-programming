a, b = int(input()), int(input())
for i in range(1,b+1):
    if a <= i*i <= b:
        print(i*i)