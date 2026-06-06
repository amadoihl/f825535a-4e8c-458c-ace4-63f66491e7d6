n = 215 
binary = []

while(n != 0):
    r = n % 2
    binary.append(r)
    n = int(n /2)

print("215 --> Base-10: ")

for i in  range(len(binary)-1,-1,-1):
    print(binary[i], end="", sep=" ")

n = 215
octal = []
while(n != 0):
    r = n % 8
    octal.append(r)
    n = int(n /8)

print("\n215 --> Base-8: ")

for i in  range(len(octal)-1,-1,-1):
    print(octal[i], end="",sep=" ")

n = 215
hex_decimal = []
while(n != 0):
    r = n % 16
    if (r == 15): hex_decimal.append('F')
    elif (r == 14): hex_decimal.append('E')
    elif (r == 13): hex_decimal.append('D')
    elif (r == 12): hex_decimal.append('C')
    elif (r == 11): hex_decimal.append('B')
    elif (r == 10): hex_decimal.append('A')
    else: hex_decimal.append(r)
    n = int(n /16)

print("\n215 --> Base-16: ")

for i in  range(len(hex_decimal)-1,-1,-1):
    print(hex_decimal[i], end="",sep = " ")
