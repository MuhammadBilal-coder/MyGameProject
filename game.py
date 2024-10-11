import random

# 0 for gun
# 1 for water
# -1 for snake

computer = random.choice([0, 1, -1])

your_turn = input("Enter your choice (gun, water, snake): ").lower()

your_dictionary = {
    "gun": 0,
    "water": 1,
    "snake": -1
}

reversed_dictionary = {
    0: "gun",
    1: "water",
    -1: "snake"
}

if your_turn in your_dictionary:
    you = your_dictionary[your_turn]

    print(f"You chose: {reversed_dictionary[you]}")
    print(f"Computer chose: {reversed_dictionary[computer]}")

    if you == computer:
        print("It's a Draw !")
    else:

        if (you == 0 and computer == -1):
            print("You win!")
        elif (you == 1 and computer == 0):
            print("You win!")
        elif (you == -1 and computer == 1):
            print("You win!")
        else:
            print("You lose!")
else:
    print("Invalid input!")
