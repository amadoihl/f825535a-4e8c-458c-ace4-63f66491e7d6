binary="101101111"

# 1's complement
ones=""

for number in binary:
    if number=="0":
        ones=ones+"1"
    else:
        ones=ones+"0"

print("1's Complement:",ones)

# 2's complement
twos=""
carry=1

for number in ones[::-1]:
    if carry==1:
        if number=="0":
            twos="1"+twos
            carry=0
        else:
            twos="0"+twos
    else:
        twos=number+twos

print("2's Complement:",twos)