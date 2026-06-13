num = ("0b1010110", "0xba2e", "0o7532")
binary = int(num[0], 2)
hexa = int(num[1],16)
octal = int(num[2],8)
print("Result are in Base 10:")
print(num[0],"--> Base 2=", binary)
print(num[1],"--> Base 16=", hexa)
print(num[2],"--> Base 8=", octal)

