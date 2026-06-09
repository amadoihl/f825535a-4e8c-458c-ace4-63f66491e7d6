a=16
b=8

print("a =",bin(a))
print("b =",bin(b))

print("AND =",bin(a&b))
print("OR =",bin(a|b))
print("XOR =",bin(a^b))
print("NOT a =",bin(~a))
print("Left Shift a =",bin(a<<1))
print("Right Shift a =",bin(a>>1))

#Even or Odd using &
n=11

if n&1:
    print(n,"is odd")
else:
    print(n,"is even")

#Clear lowest 4 bits

x=0b10111101
result=x&0b11110000
print("original =",bin(x))
print(" clearing lowest 4 bits =",bin(result))