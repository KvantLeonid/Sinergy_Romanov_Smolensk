import math

n = int(input())
k = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
j = 0
c = 0
b = 0
for i in range(n):
    j = 0
    c = 0
    if arr[i] != 1:
        d = arr[i]
        while(d > 1):
                d /= 2
                d = math.floor(d)
                j += k
        # print(j)
        d = arr[i]
        while(d != 1):
            d -= 1
            c += 1
        print(c)
        if c > j:
            b += j
        else:
            b += c
        arr[i] = 1
print(b)

# 3
# 1
# 4
# 1
# 3