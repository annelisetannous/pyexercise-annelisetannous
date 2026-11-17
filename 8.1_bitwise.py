"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in? Three permissions for a marketing campaign.
    2. What happens to it? Combine view and edit, check publish, add publish, then remove edit.
    3. What comes out? The permissions in binary at each step.
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign. View means seeing the campaign.
       Edit means changing it. Publish means making it public.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# Each permission uses a different bit.
view = 1       # Binary: 001
edit = 2       # Binary: 010
publish = 4    # Binary: 100


# Give the user permission to view and edit.
permissions = view | edit
print("View and edit:", bin(permissions))


# Check whether the user can publish.
print("Publish check:", bin(permissions & publish))

if permissions & publish:
    print("You can publish.")
else:
    print("You cannot publish.")


# Add permission to publish.
permissions = permissions | publish
print("After adding publish:", bin(permissions))


# Remove permission to edit.
permissions = permissions & ~edit
print("After removing edit:", bin(permissions))
