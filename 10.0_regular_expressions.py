"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in? A first name, a student number, and a phone number.
    2. What happens to it? Check each input against a text pattern. Save the information
      only if all three inputs are acceptable.
    3. What comes out? A confirmation message and an entry in student_details.txt, or
      an error message without saving anything.
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.
First name: one or more English letters, with no spaces, numbers, accents, or hyphens.
Student number: exactly 6 digits. Phone number: exactly 10 digits, without spaces.
WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

import re


# [A-Za-z] means an uppercase or lowercase English letter.
# + means one or more letters.
name_pattern = r"[A-Za-z]+"

# [0-9] means a digit.
# {6} means exactly six digits.
student_pattern = r"[0-9]{6}"

# [0-9] means a digit.
# {10} means exactly ten digits.
phone_pattern = r"[0-9]{10}"


# Ask for the three values.
first_name = input("Enter your first name (letters only): ")
student_number = input("Enter your student number (6 digits): ")
phone_number = input("Enter your phone number (10 digits): ")


# fullmatch checks the whole input against the pattern.
valid_name = re.fullmatch(name_pattern, first_name)
valid_student = re.fullmatch(student_pattern, student_number)
valid_phone = re.fullmatch(phone_pattern, phone_number)


# Save only when all three checks pass.
if valid_name and valid_student and valid_phone:
    with open("student_details.txt", "a", encoding="utf-8") as file:
        file.write(first_name + ";" + student_number + ";" + phone_number + "\n")

    print("Information saved successfully.")

else:
    print("Nothing was saved.")

    if not valid_name:
        print("First name: use letters only, without spaces or hyphens.")

    if not valid_student:
        print("Student number: enter exactly 6 digits.")

    if not valid_phone:
        print("Phone number: enter exactly 10 digits, without spaces.")