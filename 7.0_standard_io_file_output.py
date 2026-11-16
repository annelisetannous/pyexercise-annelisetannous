"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# A product name, a sales channel, and the quantity sold.

# 2. Process:
# Ask the user for each value and check that it is acceptable.
# Product and sales channel cannot be empty.
# Quantity must be a positive whole number.
# If an input is invalid, ask again.
# Append the entry to a CSV without deleting previous entries.
# If the file is new or empty, write the header first.

# 3. Out, file name and columns:
# File: 7.0_sales_data.csv
# Columns: product; sales_channel; quantity

# 4. Why these columns, and what this file is for:
# These columns record what was sold, where, and how many units.
# With 200 entries, I could use Excel to calculate total quantities
# by product and compare sales across channels.


# Import Python's built-in CSV module.
import csv


# Ask for a product name and reject empty input.
product = input("Enter the product name: ").strip()

while product == "":
    print("The product name cannot be empty.")
    product = input("Enter the product name: ").strip()


# Ask for a sales channel and reject empty input.
sales_channel = input("Enter the sales channel (e.g. Website): ").strip()

while sales_channel == "":
    print("The sales channel cannot be empty.")
    sales_channel = input("Enter the sales channel: ").strip()


# Ask for a positive whole number.
# If conversion fails or the number is not positive, ask again.
while True:
    try:
        quantity = int(input("Enter the quantity sold: "))

        if quantity > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Please enter a whole number, such as 5.")


# Open the file in append mode to keep previous entries.
# Append mode also creates the file if it does not exist.
with open("7.0_sales_data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    # In append mode, the position is at the end of the file.
    # A position of zero means the file is empty.
    if file.tell() == 0:
        writer.writerow(["product", "sales_channel", "quantity"])

    # Save one entry.
    writer.writerow([product, sales_channel, quantity])


print("Sales data saved successfully!")


