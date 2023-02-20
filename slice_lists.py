a = list(range(101))
print(a)

# pay attention, slice returns a copy of the list and doesn't change it
print(a[10: 20]) # 10-19
print(a[:30]) # 0-29
print(a[80:]) # 80-100
print(a[20:40:4]) # 20, 24, 28, 32, 36
print(a[::-2]) # 100, 98, 96...

