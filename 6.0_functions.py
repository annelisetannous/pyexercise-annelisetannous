"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers representing daily sales quantities for a product. 
# I reuse the original list from exercise 4.0
# 2. Process: The functions starts with a total of zero. 
# It goes through the list and adds each daily quantity to the total 
# 3. Out: The function returns the total number of units sold.
# 4. My function name, and why return rather than print:
# My function is called calculate_total_sales. The name clearly explains what it calculates.
# I use return so I can save the result in a variable and reuse it. print only displays a result; it does not return it to the caller.


# Your code below
# Define the function.
def calculate_total_sales(sales):
    total_sales = 0

    for sale in sales:
        total_sales = total_sales + sale

    return total_sales


# First call: use the original list from exercise 4.0.
daily_sales = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]
result_1 = calculate_total_sales(daily_sales)
print("Total sales for the full period:", result_1)


# Second call: use three days of sales.
# Manual check: 10 + 9 + 1 = 20.
first_three_days = [10, 9, 1]
result_2 = calculate_total_sales(first_three_days)
print("Total sales for the first three days:", result_2)


# Third call: use another period.
# Manual check: 5 + 4 = 9.
another_period = [5, 4]
result_3 = calculate_total_sales(another_period)
print("Total sales for another period:", result_3)


# Test the function with an empty list.
# It returns 0 because there are no quantities to add.
# This is acceptable: the total of an empty list is zero.
empty_sales = []
empty_result = calculate_total_sales(empty_sales)
print("Total sales for an empty list:", empty_result)
