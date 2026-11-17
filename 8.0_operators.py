"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in? Two strings: "five" and "5".
    2. What happens to it? Compare the strings using ==, !=, >, <, >=, and <=. Combine comparison results using and, or, and not.
    3. What comes out?  A table showing each expression and its True/False result.
    4. Which two values did you pick, and which comparison result surprised you? # I chose "five" and "5". 
     Both represent five to a person, but they are different text. After running, I will note which result surprised me.


WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
a = "five"
b = "5"

print("a =", a)
print("b =", b)


# Display the six comparisons.
print("Expression              | Result")
print("--------------------------------")
print("a == b                  |", a == b)
print("a != b                  |", a != b)
print("a > b                   |", a > b)
print("a < b                   |", a < b)
print("a >= b                  |", a >= b)
print("a <= b                  |", a <= b)


# Display logical combinations.
print("(a > b) and (a != b)     |", (a > b) and (a != b))
print("(a < b) or (a == b)      |", (a < b) or (a == b))
print("not (a == b)            |", not (a == b))
