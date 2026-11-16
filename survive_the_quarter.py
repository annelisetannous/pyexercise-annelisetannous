# Name: Anne-Lise Tannous
# Group letter: 
# Group number: 

# 1. WHAT GOES IN?
# The program reads scenarios_B.csv, separated by semicolons.
# It contains 14 columns: Num, Situation and four columns per option.
# Choice contains the option text. Money contains the budget change.
# Buzz contains the reputation change. Reaction contains the feedback.
# The changes are whole numbers and can be negative.
# The player enters their name and chooses A, B or C.

# 2. WHAT HAPPENS?
# Start with 10000 EUR and 50 reputation.
# Shuffle the scenarios and play up to ten days.
# Show the day, gauges, situation and options.
# Check the player's choice and apply its changes.
# Keep reputation at a maximum of 100.
# Show feedback and record the move.
# Stop immediately if either gauge reaches zero or below.

# 3. WHAT COMES OUT?
# Show the final gauges, the title and the best and worst moves.
# Explain why the player was fired, or show their final score.
# Append name, budget, reputation, title and date to results.csv.

# 4. WHAT COULD GO WRONG?
# Invalid choice: ask again. Lowercase letters are accepted.
# Empty name: ask again.
# Missing file or incorrect data: show an error and stop.
# A gauge reaches zero or below: end the game.
# Reputation exceeds 100: set it to 100.
# The result cannot be saved: show an error message.

# EXTRA FEATURE: THE ALGORITHM
# On one random day, double the reputation impact.
# I chose this feature because it adds a surprise to the game.


import csv
import random
from datetime import date


# Read the scenarios and store each option as a tuple.
def load_scenarios():
    scenarios = []

    with open("scenarios_B.csv", "r",
              encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            if not row["Situation"].strip():
                continue

            options = {}

            for letter in ["A", "B", "C"]:
                options[letter] = (
                    row[letter + "_Choice"],
                    int(row[letter + "_Money"]),
                    int(row[letter + "_Buzz"]),
                    row[letter + "_Reaction"]
                )

            scenarios.append((row["Situation"], options))

    return scenarios


# Ask for a name and reject an empty answer.
def get_name():
    name = input("Enter your name: ").strip()

    while name == "":
        name = input("Please enter your name: ").strip()

    return name


# Accept only A, B or C, including lowercase letters.
def get_choice():
    choice = input("Choose A, B or C: ").strip().upper()

    while choice not in ["A", "B", "C"]:
        choice = input("Please enter A, B or C: ").strip().upper()

    return choice


# Update the gauges and return both values as a tuple.
def apply_choice(budget, reputation, money_change, buzz_change):
    budget = budget + money_change
    reputation = reputation + buzz_change

    if reputation > 100:
        reputation = 100

    return budget, reputation


# Find the title using the rules in the brief.
def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired"

    score = reputation + budget // 200

    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Play up to ten days and record each move.
def play_game(scenarios):
    budget = 10000
    reputation = 50
    history = []

    random.shuffle(scenarios)
    algorithm_day = random.randint(1, 10)

    for day in range(1, 11):
        situation, options = scenarios[day - 1]

        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/ 100")
        print(situation)

        for letter in ["A", "B", "C"]:
            print(letter + ":", options[letter][0])

        choice = get_choice()
        text, money_change, buzz_change, feedback = options[choice]

        # Double the reputation impact on the selected day.
        if day == algorithm_day:
            buzz_change = buzz_change * 2
            print("Algorithm day! Reputation impact is doubled.")

        budget, reputation = apply_choice(
            budget, reputation, money_change, buzz_change
        )

        print(feedback)
        print("Budget impact:", money_change)
        print("Reputation impact:", buzz_change)
        print("Budget now:", budget, "EUR")
        print("Reputation now:", reputation, "/ 100")

        # Store the reputation impact first for tuple comparisons.
        history.append((buzz_change, day, text))

        if budget <= 0 or reputation <= 0:
            break

    return budget, reputation, history


# Compare the history tuples to find the best and worst moves.
def show_moves(history):
    best_move = history[0]
    worst_move = history[0]

    for move in history:
        if move > best_move:
            best_move = move
        if move < worst_move:
            worst_move = move

    print("\nBest move: day", best_move[1])
    print(best_move[2], "| Reputation impact:", best_move[0])

    print("\nWorst move: day", worst_move[1])
    print(worst_move[2], "| Reputation impact:", worst_move[0])


# Add one result without deleting results from previous games.
# Column order: name, budget, reputation, title, date.
def save_result(name, budget, reputation, title):
    with open("results.csv", "a",
              newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            budget,
            reputation,
            title,
            str(date.today())
        ])


# Run the different parts of the game in order.
def main():
    try:
        scenarios = load_scenarios()
    except OSError:
        print("Cannot open scenarios_B.csv. Check its name and folder.")
        return
    except (ValueError, KeyError, AttributeError):
        print("Check the columns and numbers in scenarios_B.csv.")
        return

    if len(scenarios) < 10:
        print("The file must contain at least ten scenarios.")
        return

    print("Welcome to Croissant Rocket!")
    name = get_name()

    budget, reputation, history = play_game(scenarios)
    title = get_title(budget, reputation)

    if title == "Fired":
        print("\nYou are fired!")

        if budget <= 0:
            print("Your budget reached zero or below.")

        if reputation <= 0:
            print("Your reputation reached zero or below.")
    else:
        print("\nQuarter survived!")
        score = reputation + budget // 200
        print("Final score:", score)

    print("Player:", name)
    print("Final budget:", budget, "EUR")
    print("Final reputation:", reputation, "/ 100")
    print("Title:", title)

    show_moves(history)

    try:
        save_result(name, budget, reputation, title)
        print("\nSaved in results.csv")
    except OSError:
        print("Your result could not be saved.")


# Handle the player interrupting the program.
try:
    main()
except (EOFError, KeyboardInterrupt):
    print("\nGame interrupted. This unfinished game was not saved.")