num = "0b101101111"

num_compliment = "0b010010000" #compliment of num
decimal = int(num_compliment, 2)
decimal += 1
print(bin(decimal))
