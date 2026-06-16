num=215
n=num
b=""
while n>0:
    b=str(n%2)+b
    n=n//2

n=num
o=""
while n>0:
    o=str(n%8)+o
    n=n//8

n=num
h=""
m="0123456789ABCDEF"
while n>0:
    h=m[n%16]+h
    n=n//16

print(num)
print(b)
print(o)
print(h)