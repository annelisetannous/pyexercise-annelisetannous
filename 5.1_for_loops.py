"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: My list of numbers in 4.0
# 2. Process: Calculate the ndouble number of list 
# 3. Out: The position, the nulber and its double for every item
# 4. What I compute for each item, and why it is worth showing:
# I calculate the double of each number.
# The reader can see the original number, its position and its double.

# Your code below
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

position = 1

for number in list_of_numbers:
    double = number * 2
    print("Position:", position, "Number:", number, "Double:", double)
    position = position + 1
