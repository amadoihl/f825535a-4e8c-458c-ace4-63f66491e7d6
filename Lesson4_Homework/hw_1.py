num = (123, 254, 503)
print("Number:\tBase:2\tBase:8\tBase:16")

for i in range(len(num)):
    print(num[i],bin(num[i]),oct(num[i]),hex(num[i]),sep="\t")