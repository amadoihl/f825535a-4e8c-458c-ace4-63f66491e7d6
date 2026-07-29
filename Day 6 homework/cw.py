#start

## CLASS ACTIVITY 1

# Write a Python program that:
#     1) Asks the user to enter a grade (as a number between 0 and 100).
#     2) Then:
#         If the input is not a number or is out of range, show an error message.
#         Otherwise, assign a letter grade:
#             A for 90 and above
#             B for 80–89
#             C for 70–79
#             D for 60–69
#             F for below 60
#     3) If the student gets an A, check if they also got a perfect score (100) and print a bonus message using a nested if.
#     4) Use a conditional expression to quickly determine if the grade is a "Pass" or "Fail" (60 is the passing score).
#     5) What happens if the user enters 0 or an empty string?

## Please complete the code using the following template

grade_input = input("Enter your grade (0-100): ")

# Corner case: empty input
if grade_input=="":  # <check if the value is empty>
    print("You didn't enter anything.")
else:
    # Check if input is a valid number
    if grade_input.isdigit():
        # Don't forget to do what we learn in the previous class before comparing the input
        grade=int(grade_input)

        # Check valid ran

        if grade >= 0 and grade <= 100:
            print("you entered ",grade)
            # Grading with elif
            if grade ==100:  # <add code>
                print("Perfect score!")
                    
            if grade >=90:   # <add code>
                final_grade = "A"
            elif grade >=80 :   # <add code>
                final_grade = "B"
            elif grade >=70 :   # <add code>
                final_grade = "C"
            elif grade >=60:  # <add code>
                final_grade = "D"
            else :
                final_grade= "F" # <add code>

            # <Complete the rest of the if statements to assign the final_grade>

            print("Letter grade:", final_grade)

            # Conditional Expression for Pass/Fail
            result = "pass" if grade >= 60 else "fail" # <Complete this code>
            print("Result:", result)

        else:
            print("Grade must be between 0 and 100.")
    else:
        print("Invalid input. Please enter a number.")


####################################################################
####################################################################
####################################################################


## CLASS ACTIVITY 2

# You are writing the program that decides who can board the roller coaster called The Cyclone, 
# and how much each rider pays. Build it one step at a time.

# 1) Collect the rider's details. Ask for and store:
#     - height in cm
#     - age
#     - whether an adult is with them (yes or no)
#     - whether they have a season pass (yes or no)
#     - the day of the week, such as Monday

    height =int(input("enter your height in cm"))
    age=int(input("enter your age"))
    adult=input("are u with adult (yes/no)")
    passs=input("do u have season passs (yes/no)")
    day=input("enter the day of the week")







# 2) Decide if they can board, using a nested if:
#     - Shorter than 120 cm: print a message and stop here, since they cannot ride.
#     - From 120 to 139 cm: they can ride only if an adult is with them.
#     - 140 cm or taller: they can ride.


    if height<120:
        print("you cannot ride")
    elif height>=120 and height<=139:
        print ("only if adult is with you")
    else:
        print("you can ride sudip")

# 3) Set the ticket price with an elif chain, based on the rider's age:
#     - 5 to 12: $15
#     - 13 to 17: $25
#     - 18 to 64: $40
#     - 65 or older: $30
# Children under 5 are not allowed on this ride.

    if age>5 and age<=12:
        price=15
    elif age>=13 and age<=17:
        price=25
    elif age>=18 and age<=64:
        price=40
    elif age>=65 :
        price=30
    else:
        print("you cannot ride cause Children under 5 are not allowed on this ride.")




# 4) Add a weekend additional charge using a conditional expression on a single line. 
#    Add $10 to the price if the day is Saturday or Sunday, and nothing otherwise.

    day_loweredcase=day.lower()
    price +=10 if day_loweredcase=="saturday" or day_loweredcase=="sunday" else 0





# 5) Decide the fast pass with a nested if that uses and and or. A rider skips the line 
#    if they have a season pass and (the day is a weekday or the rider is 65 or older). 
#    Print whether they get the fast pass or wait in line.

    if passs=="yes" and (day_loweredcase!="saturday" and day_loweredcase!="sunday" or age>=65):
        print("you get fast pass")
    else :
        print("wait in line")





# 6) Bonus: Why should the height check come first? What could go wrong if you set the 
#    ticket price before checking whether the rider is allowed on the ride at all?

#cause it will be unfair