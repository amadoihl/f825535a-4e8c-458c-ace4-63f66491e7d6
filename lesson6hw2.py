#using modulo operation
price = float(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
name = input("Name of item purchased: ")

total = price * quantity
print("%d %s at Rs. %.2f each and Total Cost: Rs. %.2f" %
      (quantity, name, price, total))



#using str.format
price = float(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
name = input("Name of item purchased: ")

total = price * quantity


print("{} {} at Rs. {:.2f} each and Total Cost: Rs. {:.2f}".format(
    quantity, name, price, total))




#using f-strings
price = float(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
name = input("Name of item purchased: ")

total = price * quantity

print(f"{quantity} {name} at Rs. {price:.2f} each and Total Cost: Rs. {total:.2f}")




#using template strings
from string import Template

price = float(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
name = input("Name of item purchased: ")

total = price * quantity

receipt = Template(
    "$qty $item at Rs. $price each and Total Cost: Rs. $total"
)

print(receipt.substitute(
    qty=quantity,
    item=name,
    price=f"{price:.2f}",
    total=f"{total:.2f}"
))