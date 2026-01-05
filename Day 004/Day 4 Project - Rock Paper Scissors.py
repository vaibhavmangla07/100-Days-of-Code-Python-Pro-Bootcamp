import random

Rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [Rock, Paper, Scissors]

print("Welcome To The Rock, Paper and Scissors Game")
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userChoice >= 0 and userChoice <= 2:
    print(gameImages[userChoice])

compChoice = random.randint(0, 2)
print("Computer Choice : ")
print(gameImages[compChoice])

if userChoice >= 2 or userChoice < 0:
    print("You Entered Invalid Number!")
elif userChoice == 0 and compChoice == 2:
    print("You Win!!!")
elif compChoice == 0 and userChoice == 2:
    print("You lose!!!")
elif compChoice > userChoice:
    print("You Lose!!!")
elif compChoice == userChoice:
    print("Draw")


