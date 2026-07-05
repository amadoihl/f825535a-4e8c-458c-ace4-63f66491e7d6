a = 7
b = 11
c = 4
d = '4'

print(a < 0b100)
 # false --> 7<4 is not true
print( a + c <= b)
 #11 <=11 --> True

print(c!=d)
 # True --> integer is never equal to string

print(b-a>c)
 #4>4 --> False

print(b-a>=c)
 #4=4 --> True

print(c!=int(d))
 #4 is not equal to 4 --> False

print(b-a == int(d))
 #4=4 --> True