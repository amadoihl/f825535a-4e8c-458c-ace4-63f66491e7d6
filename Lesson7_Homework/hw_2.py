name = input("Enter Item Name:  ")
price = float(input("Enter Price of Item: "))
quantity = float(input("Enter Quantity of Item: "))
total = quantity * price
tax = float(input("Enter Tax Rate: "))
total += total *(tax/100)
charges = 0
choice = input("Pay Via Card?(y/n)")
if(choice.lower() == "y"):
    print("Note: 3% charge is applicable for Card Payment:")
    charges = 3
    total += total *(3/100)

#f string
print(f"\n{quantity} {name} Purchased @ {price} Rs. each.")
print(f"Tax: {tax}\nCard Charge: {charges} %\nTotal: Rs.{total}.")


