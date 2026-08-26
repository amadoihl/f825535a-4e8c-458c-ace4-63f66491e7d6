# Class Activity

################################################################################
## 1) Define a function greet(name) that RETURNS "Hello, <name>"
# <define function here>

print(greet("IHL")) # expected: Hello, IHL

################################################################################
## 2) Define log(msg) that prints "LOG: <msg>" and does not return anything.
# <define function here>

x = log("saving...")
print(x is None)          # expected: True

################################################################################
## 3) Define my_len(seq) WITHOUT using len(); count with a loop.
# <define function here>

print(len("python"), my_len("python"))  # expected: 6 6

################################################################################
## 4)  Define area(width, height) and call it with arguments 3 and 4.
# <define function here>

print(area(3, 4))  # expected: 12

################################################################################
## 5) Define order_pizza(size, crust, topping) → "<size> <crust> with <topping>"
# <define function here>

print(order_pizza(12, "thin", "mushrooms"))
print(order_pizza(topping="pepperoni", crust="stuffed", size=16))
# expected:
# 12 thin with mushrooms
# 16 stuffed with pepperoni

################################################################################
## 6) Define power(base, exp=2) that returns base**exp; test both forms.
# <define function here>

print(power(5), power(2, 3))  # expected: 25 8

################################################################################
## 7) Use a global counter and increment it inside a function.
# <define function here>

counter = 0
increment()
increment()
print(counter)  # expected: 2
