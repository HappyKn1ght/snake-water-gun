# Snake Water Gun Game

import random
def print_line():
    print("-" * 40)

user_score = 0
computer_score = 0
draw = 0

print("Snake Water Gun Game")
print("1 for Snake\n2 for Water\n3 for Gun")

choice = {1: "Snake", 2: "Water", 3: "Gun"}

while True:

    user_input = input("Enter Your Choice or 'q' to quit: ").lower().strip()
    if user_input == "q":
        break

    try:
        user_input = int(user_input)
        if user_input not in choice:
            print("Out of range! Please choose 1, 2, or 3.")
            continue

        print(f"You chose {choice[user_input]}")
        computer = random.randint(1, 3)
        print(f"Computer Chose {choice[computer]}")

        if user_input == computer:
            draw += 1
            print(f"Both Chose {choice[user_input]}\nIt's a draw!")

        elif (
            (user_input == 1 and computer == 2)
            or (user_input == 2 and computer == 3)
            or (user_input == 3 and computer == 1)
        ):
            user_score += 1
            print("You Win!")
        else:
            computer_score += 1
            print("Computer Wins!")
            
    except ValueError:
        print("Invalid Input!")
        continue

    again = input("Do you want to try again? (y/n): ").lower().strip()
    if again != "y":
        break

print_line()
print("FINAL SCOREBOARD")
print_line()

print(f"User Score  Computer Score  Match Draw\n   {user_score}\t\t  {computer_score}\t\t{draw}\n")
if user_score > computer_score:
    print_line()
    print("🏆 You Are the Overall Winner!")
    print_line()
elif user_score < computer_score:
    print_line()
    print("💻 Computer Wins the Match!")
    print_line()
else:
    print_line()
    print("🤝 Overall Match Draw!")
    print_line()

print("\nGAME OVER...\nThanks for playing!") 
