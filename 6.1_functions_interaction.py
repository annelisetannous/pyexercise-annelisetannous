"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:An intenger entered by the user

# 2. Process, function by function:
# is_zero checks whether the number is zero.
# is_positive checks whether the number is greater than zero.
# is_even checks whether the number is divisible by two.
# detailed_message uses these functions to describe the number.

# 3. Out:
# A message describing whether the number is positive, negative,
# or zero, and whether it is even or odd.

# 4. The question my fourth function answers:
# "How can I describe this number?"
# Splitting the checks into three functions makes them easier to test.
# I can check each result separately before using them together.


# Check whether the number is zero.
def is_zero(number):
    return number == 0


# Check whether the number is positive.
def is_positive(number):
    return number > 0


# Check whether the number is even.
def is_even(number):
    return number % 2 == 0


# Test each small function separately before combining them.

# Test 1: input = 0, expected output = True.
print("Zero check (expected True):", is_zero(0))

# Test 2: input = -3, expected output = False.
print("Positive check (expected False):", is_positive(-3))

# Test 3: input = 4, expected output = True.
print("Even check (expected True):", is_even(4))


# Combine the three checks to build one message.
def detailed_message(number):
    if is_zero(number):
        sign = "zero"
    elif is_positive(number):
        sign = "positive"
    else:
        sign = "negative"

    if is_even(number):
        parity = "even"
    else:
        parity = "odd"

    return "The number is " + sign + " and " + parity + "."


# Ask the user for an integer and display the description.
number = int(input("Enter a whole number: "))
print(detailed_message(number))


