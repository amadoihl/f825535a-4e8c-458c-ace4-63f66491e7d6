name = input("Enter Item Name:  ")
price = float(input("Enter Price of Item: "))
quantity = float(input("Enter Quantity of Item: "))
total = quantity * price


taxes = float(input("Enter Tax Rate: "))
total += total *(taxes/100)
charge = 0
choice = input("Pay Via Card?(y/n)")
if(choice.lower() == "y"):
    print("5% charge for Card Payment:")
    charge = 5
    total += total *(5/100)


print(f"\n{quantity} {name} Purchased @ {price} Rs. each.")
print(f"Tax: {taxes}\nCard Charge: {charge} %\nTotal: Rs.{total}.")