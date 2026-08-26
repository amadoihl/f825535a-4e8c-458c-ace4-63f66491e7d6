# Class Activity - Catch the Error!
#
# Goal: when you are done, this file should run from top to bottom without
# crashing, and print the expected lines shown under each part.
#
# Work one part at a time and run the file often. Right now it stops at
# part 1, and that is normal.
#
# Exceptions you may need:
#   ZeroDivisionError, IndexError, KeyError, TypeError, ValueError,
#   NameError, LookupError, ArithmeticError, OverflowError, Exception


################################################################################
##                        A) Warm up: catch the exception                     ##
################################################################################

################################################################################
## 1) Division by zero
#     Which exception happens here? Wrap the print in a try-except so the
#     program keeps going.

print(10 / 0)

# expected: Cannot divide by zero


################################################################################
## 2) Accessing a missing list element

numbers = [1, 2, 3]
print(numbers[5])

# expected: That index does not exist


################################################################################
## 3) Using the wrong type

print("Hello" + 5)

# expected: Cannot add a string and a number


################################################################################
## 4) Converting invalid data

age = int("twenty")

# expected: That is not a whole number


################################################################################
## 5) Accessing a missing dictionary key
#     Catch the exception, and add a finally block as well. The finally block
#     has to run whether the key is there or not. Test it both ways.

person = {"name": "Alice"}
print(person["age"])

# expected:
# There is no key called 'age'
# Done looking up the person


################################################################################
##                    B) Choosing and ordering the branches                   ##
################################################################################

################################################################################
## 6) One try, several except branches
#     show_score can fail in three different ways depending on what you pass
#     it. Write one try-except with three except branches so that each call
#     below prints the right message.
#
#       KeyError   -> "No student called <name>"
#       IndexError -> "<name> has no score at position <position>"
#       TypeError  -> "The position must be a number"

scores = {"amy": [90, 85], "ben": []}

def show_score(name, position):
    # TODO: put the try-except here
    print(scores[name][position])

show_score("zoe", 0)
show_score("ben", 0)
show_score("amy", "first")

# expected:
# No student called zoe
# ben has no score at position 0
# The position must be a number


################################################################################
## 7) The order of the branches matters
#     This prints the same message no matter what goes wrong. Work out why,
#     then fix it so the ZeroDivisionError branch is the one that runs.

def divide(a, b):
    try:
        print(a / b)
    except Exception:
        print("Something went wrong")
    except ZeroDivisionError:
        print("You cannot divide by zero")

divide(10, 0)

# Why does the second branch never run?
# Your answer:

# expected after your fix: You cannot divide by zero


################################################################################
## 8) Reading the message out of the exception
#     Use "as e" so you can print what Python actually says, instead of
#     making up your own wording.

def to_int(text):
    return int(text)

# TODO: call to_int("abc") inside a try-except ValueError as e,
#       and print "Could not convert: <the message from e>"

# expected:
# Could not convert: invalid literal for int() with base 10: 'abc'


################################################################################
## 9) The default except has to be last
#     Uncomment the block below and run the file.
#     Notice that nothing runs at all, not even part 1. Read the error and
#     say why. Then reorder the branches so the file runs again.

# try:
#     print(undefined_variable)
# except:
#     print("Something is wrong...")
# except NameError:
#     print("That variable does not exist")

# Why did part 1 not run this time?
# Your answer:

# expected after your fix: That variable does not exist


################################################################################
##                       C) finally, and checking first                       ##
################################################################################

################################################################################
## 10) finally runs even when the function returns
#      Write down what you think this prints BEFORE you run it, then run it.

def risky(n):
    try:
        return 100 / n
    except ZeroDivisionError:
        return "undefined"
    finally:
        print("finally ran")

print(risky(4))
print(risky(0))

# Your prediction:

# expected:
# finally ran
# 25.0
# finally ran
# undefined


################################################################################
## 11) Checking first vs handling afterwards
#      Version A checks the types before doing the work.
#      Write version B, which just tries the subtraction and handles the
#      TypeError. Both versions must print the same thing.

def subtract_a(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    else:
        return "Invalid data types"

def subtract_b(a, b):
    # TODO: same result, but with try-except instead of isinstance
    return None

print(subtract_a(10, 3))
print(subtract_a(10, "3"))
print(subtract_b(10, 3))
print(subtract_b(10, "3"))

# expected:
# 7
# Invalid data types
# 7
# Invalid data types


################################################################################
##                     D) Exceptions and function boundaries                  ##
################################################################################

################################################################################
## 12) The exception travels up through the callers
#      func3 divides by zero. Nobody handles it in func2 or func1, so it
#      keeps going up until it reaches the top and stops the program.
#      Add ONE try-except, in the right place, so the message is printed
#      instead of the traceback.
#      Do not change func1, func2 or func3.

def func1():
    return func2()

def func2():
    return func3()

def func3():
    return 1 / 0

func1()

# expected: Caught at the top: division by zero


################################################################################
## 13) Handling it here, or passing it on
#      load_age swallows the ValueError and returns None, so the caller never
#      finds out anything went wrong.
#      Change load_age so it prints its note and then passes the exception on
#      to the caller.
#      Hint: a plain "raise" inside an except block re-raises what you caught.

def load_age(text):
    try:
        return int(text)
    except ValueError:
        print("load_age: bad input")
        return None

try:
    print(load_age("41"))
    print(load_age("forty one"))
except ValueError:
    print("The caller decided to stop here")

# expected after your change:
# 41
# load_age: bad input
# The caller decided to stop here


################################################################################
##                          E) The exception hierarchy                        ##
################################################################################

################################################################################
## 14) Catching the parent catches the children
#      LookupError is the parent of both IndexError and KeyError.
#      ArithmeticError is the parent of ZeroDivisionError and OverflowError.
#      Replace the two except branches in each function with a single branch,
#      without changing anything that gets printed.

import math

def fetch(container, key):
    try:
        return container[key]
    except IndexError:
        return "lookup failed"
    except KeyError:
        return "lookup failed"

def compute(n):
    try:
        return math.exp(10 / n)
    except ZeroDivisionError:
        return "math failed"
    except OverflowError:
        return "math failed"

print(fetch([1, 2, 3], 9))
print(fetch({"a": 1}, "b"))
print(compute(0))
print(compute(0.001))

# expected:
# lookup failed
# lookup failed
# math failed
# math failed


################################################################################
## 15) Raising an exception yourself
#      check_age should raise a ValueError with the message
#      "Age cannot be negative" when it is given a negative number.
#      Use the raise keyword.

def check_age(age):
    # TODO
    return age

for value in [30, -5]:
    try:
        print(check_age(value))
    except ValueError as e:
        print(f"Rejected: {e}")

# expected:
# 30
# Rejected: Age cannot be negative


################################################################################
##                            F) Stretch: debugging                           ##
################################################################################

################################################################################
## 16) Find the bug with the debugger
#      average() gives the wrong answer. Do not just read it, use the
#      debugger. From the terminal, run:
#
#          python -m pdb inclass.py
#
#      Use n to step to the next line and p total to print a variable.
#      Watch total while the loop runs, then fix the function.

def average(values):
    total = 0
    count = 0
    for v in values:
        total = v
        count = count + 1
    return total / count

print(average([2, 4, 6]))

# expected once fixed: 4.0
