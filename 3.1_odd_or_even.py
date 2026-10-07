"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The number N is used 
# 2. Process: We are asking the code if the others numbers are pair or not  N
# 3. Out: The program is telling us if the number is pair or not. 
# 4. What happens on 0, on a negative number, on a very large number:
#For 0, it displays a 0
#For a negative number it says it with a "-" before
#For a large number, it runs normally 


# Your code below

number = int(input("Enter a number: "))

if number == 0:
    print("0 is zero")

elif number < 0:
    print(number, "is a negative number")

else:
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")