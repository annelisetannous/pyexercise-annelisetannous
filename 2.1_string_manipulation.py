"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the sentence the user is putting on the code
# 2. Process: Having four ways of writing a sentence
# 3. Out: four difference way of writing a sentence
# 4. My four transformations, and when each is useful:


# Your code below

sentence=input("Enter a sentence")

result_1 = sentence.strip()
print("without extra spaces:", result_1)

result_2 = sentence.lower()
print("lowercase:", result_2)

result_3 = sentence.upper()
print("uppercase:", result_3)

result_4 = sentence.title()
print("title:", result_4)