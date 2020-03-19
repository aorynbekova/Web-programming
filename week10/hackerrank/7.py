n = int(input())
array = list(map(int, input().split()))
print(max([x for x in array if x != max(array)]))