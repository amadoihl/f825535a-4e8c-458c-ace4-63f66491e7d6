num=215

# Binary Conversion
n=num
bina=""

while n>0:
    remr=n%2
    bina=str(remr)+bina
    n=n//2

print("Binary:",bina)

# Octal Conversion
n=num
octal=""

while n>0:
    remr=n%8
    octal=str(remr)+octal
    n=n//8

print("Octal:",octal)

# Hexadecimal Conversion
n=num
hexa=""
digits="0123456789ABCDEF"

while n>0:
    remr=n%16
    hexa=digits[remr]+hexa
    n=n//16

print("Hexadecimal:",hexa)