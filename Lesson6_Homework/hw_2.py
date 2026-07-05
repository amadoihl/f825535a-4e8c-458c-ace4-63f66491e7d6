name = input("Enter Item Name:  ")
price = float(input("Enter Price of Item: "))
quantity = float(input("Enter Quantity of Item: "))
total = quantity * price

# modulus operator
print("%.3f %s purchased @ %.3f Rs. each" %(quantity, name, price))
print("Total Cost: %.3f Rs." % (total))

#str.format
print("{} {} purchased @ {} Rs. each.".format(quantity,name,price))
print("Total Cost: {} Rs.".format(total))

#f string
print(f"{quantity} {name} purchased @ {price} Rs. each.")
print(f"Total Cost:{total} ")

#template strings
from string import Template
template = Template("$qty $item_name purchased @ $pr Rs. each.\nTotal Cost: $total Rs.")
receipt_template = template.substitute(
    qty=quantity,
    item_name=name,
    pr=price,
    total=total
)
print(receipt_template)
