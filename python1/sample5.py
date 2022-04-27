a = 3127
b = 8201
max = 0

for i in range(a):
    if i == 0: continue
    max = i if a % i == 0 and b % i == 0 else max
print(max)