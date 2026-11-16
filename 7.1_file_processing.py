"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# Capitalization is inconsistent, for example "ada LOVELACE".
# Some lines have leading spaces, for example "  alan TURING".
# There are two empty lines.
#"GUIDO van rossum" has three words, so its last name needs
#special attention: "van rossum" must stay together.


# 1. In:The names stored in names.txt.
# 2. Process, problem by problem:
# Remove unnecessary spaces using split and join.
# Skip empty lines.
# Standardize capitalization using title.
# Treat everything after the first name as the last name.
# Sort by that last name and save to a different file.

# 3. Out:
# A new file called sorted_names.txt containing eight cleaned names.
# The original names.txt file is not modified.
# 4. How I decide which word is the last name:
# For this file, I assume the first word is the first name.
# Everything after it is the last name.
# For "Ada Lovelace", the last name is "Lovelace".
# For "Guido Van Rossum", the last name is "Van Rossum".
# This is a rule for this dataset, not for every possible name.


# Your code below
# Read the original file.
with open("names.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


# Clean the names and skip empty lines.
cleaned_names = []

for line in lines:
    name = " ".join(line.split())

    if name != "":
        name = name.title()
        cleaned_names.append(name)


# Return the last name to use for sorting.
def get_last_name(name):
    return name.split(" ", 1)[1].lower()


# Sort alphabetically by the complete last name.
cleaned_names.sort(key=get_last_name)


# Write the cleaned names to a new file.
with open("sorted_names.txt", "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")


# Display checks.
print("Original number of lines:", len(lines))
print("Number of saved names:", len(cleaned_names))
print("Number of empty lines removed:", len(lines) - len(cleaned_names))

if cleaned_names:
    print("First name in the sorted list:", cleaned_names[0])
    print("Last name in the sorted list:", cleaned_names[-1])

print("Cleaned names saved to sorted_names.txt")