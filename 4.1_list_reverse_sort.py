"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: My orginal list from 4.0 exercise
# 2. Process: Display the list in four different wats
# 3. Out: Four differents orders and the list of origin at the end
# 4. My four orders, and which ones modify the original:
# sorted(): ascending order, does not modify the original list
# sorted(reverse=True): descending order, does not modify the original list
# reversed(): reversed order, does not modify the original list
# slicing [::-1]: reversed order, does not modify the original list

# Your code below
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

# First order: ascending
order_1 = sorted(list_of_numbers)
print("Ascending order:", order_1)

# Second order: descending
order_2 = sorted(list_of_numbers, reverse=True)
print("Descending order:", order_2)

# Third order: reverse of the original list
order_3 = list(reversed(list_of_numbers))
print("Reversed original order:", order_3)

# Fourth order: even numbers first, then odd numbers
order_4 = sorted(list_of_numbers, key=lambda x: x % 2)
print("Even numbers first:", order_4)

# Prove that the original list has not changed
print("Original list:", list_of_numbers)