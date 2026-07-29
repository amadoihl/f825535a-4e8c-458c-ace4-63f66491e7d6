
# % 
price = int(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
item = input("Name of item purchased: ")

total = price * quantity

print("%d items @ %d Rs. each | Total Cost: %d Rs." % (quantity, price, total))

#str format 

price = int(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
item = input("Name of item purchased: ")

total = price * quantity

print("{} items @ {} Rs. each | Total Cost: {} Rs.".format(quantity, price, total))

# f string

price = int(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
item = input("Name of item purchased: ")

total = price * quantity

print(f"{quantity} items @ {price} Rs. each | Total Cost: {total} Rs.")


#Templete

from string import Template

price = int(input("Item price in Rs.: "))
quantity = int(input("Quantity purchased: "))
item = input("Name of item purchased: ")

total = price * quantity

receipt = Template("$quantity items @ $price Rs. each | Total Cost: $total Rs.")

print(receipt.substitute(
    quantity=quantity,
    price=price,
    total=total
))