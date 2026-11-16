# Snake Water Gun Game

import random

print("Snake Water Gun Game")
print("1 for Snake\n2 for Water\n3 for Gun")

choice = {1: "Snake", 2: "Water", 3: "Gun"}

user_input = int(input("Enter Your Choice: "))
print(f"You chose {choice[user_input]}")
computer = random.randint(1,3)
print(f"Computer Chose {choice[computer]}")

if user_input == computer:
    print(f"Both Chose {choice[user_input]}\nIt's a draw!")

elif ((user_input == 1 and computer == 2) or
      (user_input == 2 and computer == 3) or
      (user_input == 3 and computer == 1)):
    print("You Win!")
else:
    print("Computer Wins!")