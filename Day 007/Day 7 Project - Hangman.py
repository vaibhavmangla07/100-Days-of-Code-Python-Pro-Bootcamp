import random
from HangmanWords import wordList
from HangmanArt import stages, logo, youWin, youLose

lives = 6

print(logo)

chooseWord = random.choice(wordList)
# print(chooseWord)

placeholder = ""
for pos in range(len(chooseWord)) :
    placeholder += "_"
print(placeholder)

gameOver = False
correctLetter = []

while not gameOver:
    print(f"****************************{lives}/6 LIVES LEFT*******************************")

    guess = input("Guess a word : ").lower()
    if guess in correctLetter:
        print(f"You've already guessed! {guess}")

    display = ""

    for letter in chooseWord:
        if letter == guess:
            display += letter
            correctLetter.append(guess)
        elif letter in correctLetter:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chooseWord:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            gameOver = True
            print(youLose)

    if "_" not in display:
        gameOver = True
        print(youWin)

    print(stages[lives])
