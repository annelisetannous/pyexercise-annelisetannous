"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in? A number entered by the user.
    2. What happens to it? Divide 100 by the number. If the input is invalid, display a
     message and ask again. Allow unlimited attempts until the calculation succeeds.

    3. What comes out? The result of the division, or a helpful error message.
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding. ValueError: the input cannot be
         converted to a number. ZeroDivisionError: the user enters zero. Separate 
         messages explain exactly what the user needs to fix. Catching these errors
         separately also avoids hiding unrelated bugs.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. The two failures, and whether they deserve the same message:


# Your code below
while True:
    try:
        number = float(input("Enter a number other than zero: "))
        result = 100 / number
        print("Result:", result)
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

    except ZeroDivisionError:
        print("You cannot divide by zero. Please try another number.")