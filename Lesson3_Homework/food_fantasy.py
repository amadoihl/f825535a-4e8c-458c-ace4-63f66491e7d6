#Food Fantasy Market!

print("Welcome to the Fantasy Food Market!")
print("Enter Your Coin Details:")
print("--------------------------------------")
bronze_coin = int(input("Enter Bronze Coins: "))
silver_coin = int(input("Enter Silver Coins: "))
gold_coin = int(input("Enter Gold Coins: "))
total_gold_coin = gold_coin + silver_coin/10 + bronze_coin/1000 #converting all coins into gold coins
print("\nYour Total:", round(total_gold_coin,2), "Gold Coins")
choice = "Noexit"
items = ""
while (choice != "exit") :
    print("\n\t Menu:")
    print("-------------------------")
    print("Items\tPrice(Equivalent Gold Coins)")
    print("Bread\t0.75")
    print("Cheese\t1.5")
    print("Apple\t0.25")
    print("Roast Chicken\t3.2")
    print("Pie\t2.4")
    choice = input("\nWhat would you like to buy?(type 'exit' to finish): ") #input for choice from menu
    choice = choice.lower()  #converting choice into lowercase to easy comparision
    if choice == "exit":
        break                #going out from loop
    elif choice == "bread":
        if total_gold_coin >= 0.75:    #checking if balance is sufficient for the purchase
             total_gold_coin -= 0.75   #updating new balance by decreasing it by purchase value
             items = items + " Bread"  #concating string
             print("You Bought Bread for 0.75 gold.\n","Remaining Balance:", round(total_gold_coin,2))
        else:
            print("You Cannot afford Bread! You have", round(total_gold_coin,2), "gold")
       
    elif choice == "cheese":
        if total_gold_coin >= 1.5: 
             total_gold_coin -= 1.5
             items = items + " Cheese,"
             print("You Bought Cheese for 1.5 gold.\n","Remaining Balance:", round(total_gold_coin,2))
        else:
            print("You Cannot afford Cheese! You have", round(total_gold_coin,2), "gold")

    elif choice == "apple":
        if total_gold_coin >= 0.25: 
             total_gold_coin -= 0.25
             items = items + " Apple,"
             print("You Bought Apple for 0.25 gold.\n","Remaining Balance:", round(total_gold_coin,2))
        else:
            print("You Cannot afford Apple! You have", round(total_gold_coin,2), "gold")
        
    elif choice == "roast chicken":
        if total_gold_coin >= 3.2: 
             total_gold_coin -= 3.2
             items = items + " Roast Chicken,"
             print("You Bought Roast Chicken for 3.2 gold.\n","Remaining Balance:", round(total_gold_coin,2))
        else:
            print("You Cannot afford Roast Chicken! You have", round(total_gold_coin,2), "gold")
        
    elif choice == "pie":
        if total_gold_coin >= 2.4: 
             total_gold_coin -= 2.4
             items = items + " Pie,"
             print("You Bought Pie for 2.4 gold.\n","Remaining Balance:", round(total_gold_coin,2))
        else:
            print("You Cannot afford Pie! You have", round(total_gold_coin,2), "gold")
    else:
        print("Invalid Choice. Retry!")   #informing user about thier choice if the choice isnot present Menu

print("\n---Shopping Summary---")
print("Items Purchased: ",items)
print("Final Balance:", round(total_gold_coin,2))  #shows new balance after purchase
print("Equivalent to -->")
#converting new balance to all coins
new_gold_coin = int(total_gold_coin)
new_silver_coin = int(total_gold_coin*10)
new_bronze_coin = int(total_gold_coin*1000)
print("\t\t",round(new_gold_coin,2) ,"Gold,", round(new_silver_coin,2), "Silver,", round(new_bronze_coin,2) ,"Bronze")
print("Thank You For Visiting!")







