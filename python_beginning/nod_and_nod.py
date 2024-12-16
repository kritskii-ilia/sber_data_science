a = int(input())
b = int(input())
d = a*b
s = 0
while d != 0:
    if d % a == 0 and d % b == 0:
        s = d
    d-=1
print(s)