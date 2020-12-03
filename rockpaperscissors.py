import images
import random

hand_signals = [images.rock, images.paper, images.scissors]

print("Welcome to Rock, Paper, Scissors")
user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))

print(f"You threw\n {hand_signals[user_hand]}")

computer_hand = random.randint(0,2)
print(f"Computer threw\n {hand_signals[computer_hand]}")

if hand_signals[user_hand] == hand_signals[computer_hand]:
  print("It's a draw!") 
elif hand_signals[user_hand] == 0 and hand_signals[computer_hand] == 2:
  print("You win!")
elif hand_signals[user_hand] == 1 and hand_signals[computer_hand] == 0:
  print("You win!")
elif hand_signals[user_hand] == 2 and hand_signals[computer_hand] == 1:
  print("You win!")
else:
  print("You lost!")