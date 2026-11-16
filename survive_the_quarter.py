# Name: Anne-Lise Tannous
# Group letter:
# Group number:


# 1. WHAT GOES IN?
# I use scenarios_B.csv for my game.
# The file has 14 columns separated by semicolons.
# Num is the scenario number and Situation is the story.
# For each choice, I read its text, money change, reputation change
# and feedback. The numbers can be positive, negative or zero.
# For example, option B uses B_Choice, B_Money, B_Buzz and B_Reaction.
# The player provides their name and their choices during the game.

# 2. WHAT HAPPENS?
# I start the player with 10000 EUR and 50 reputation.
# I shuffle the scenarios so the order can change between games.
# Each day, I show the situation, the gauges and the three choices.
# I check the answer before updating the budget and reputation.
# I display the feedback and keep the move in the history.
# Reputation cannot go above 100.
# The player loses if either gauge reaches zero or below.
# Otherwise, the game continues until the end of day ten.

# 3. WHAT COMES OUT?
# At the end, the player sees their remaining budget and reputation.
# If they lose, I explain which gauge caused them to be fired.
# If they survive, I calculate their score and display their title.
# I also show the moves with the highest and lowest reputation impacts.
# I save one row in results.csv with the player's name, budget,
# reputation, title and date. I keep the results of earlier games.

# 4. WHAT COULD GO WRONG?
# A player might type something other than A, B or C.
# I ask again, and I also accept lowercase letters.
# I ask again if the player leaves their name empty.
# If the CSV cannot be opened, I show a message and stop.
# I also stop with a message if a column or number is incorrect.
# I check the gauges after each choice so the game ends immediately
# when the player runs out of money or reputation.
# If saving fails, I tell the player that the result was not saved.

# MY EXTRA FEATURE: THE ALGORITHM
# I chose the algorithm feature to add a surprise during the game.
# On one random day, the reputation impact is doubled.
# A positive impact becomes more helpful, but a negative one
# becomes more damaging.gauge reaches zero or below: end the game.
# Reputation exceeds 100: set it to 100.
# The result cannot be saved: show an error message.




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