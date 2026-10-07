# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-07 12:05, in .

**Me:** how to print a statement in python

**Tutor:**

Printing a statement in Python is done with the `print()` function.

```python
# Print a single statement
print("Hello, world!")
```

What is the argument you pass to `print()` to display text?

**Me:** How do I transform a sentence in different ways in Python?

**IA:** You can use string methods such as `.strip()`, `.lower()`, `.upper()` and `.title()`.


**Me:** Why can't I do calculations directly with input()?

**IA:** `input()` returns text. You can convert it to a number using `int()` or `float()` before doing calculations.


**Me:** How can I avoid dividing by zero?

**IA:** Check the second number with an `if` statement before dividing:
`if number_2 != 0:`


**Me:** How can I check if a number is odd or even?

**IA:** Use the modulo operator `%`. If `number % 2 == 0`, the number is even. Otherwise, it is odd.


**Me:** How can I check every number from 1 to N?

**IA:** You can use a `for` loop with `range(1, number + 1)`.


**Me:** How can I sort a list without changing the original list?

**IA:** Use `sorted()` instead of `.sort()`. You can also use `reverse=True` for descending order and `[::-1]` to reverse the list.


**Me:** How can I do the same calculation for every number in a list?

**IA:** Use a `for` loop. Put the calculation inside the loop so it is repeated for every item.


**Me:** How can I display the position of every item?

**IA:** Start with `position = 1` and increase it inside the loop with `position = position + 1`.


**Me:** How can I stop a while loop after 10 attempts?

**IA:** Use a counter and include `i < 10` in the condition. Increase `i` after each attempt.


**Me:** How can I accept "YES", "Yes" and " yes " as the same answer?

**IA:** Use `.strip().lower()` on the answer. `.strip()` removes extra spaces and `.lower()` converts the text to lowercase.

