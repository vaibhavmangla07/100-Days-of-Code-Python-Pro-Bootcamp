from art import logo, vs
from GameData import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_description}, from{account_country}"

def check(user_guess, followersA, followersB):
    if followersA > followersB:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
should_continue = True

while should_continue:
    accountA = random.choice(data)
    accountB = random.choice(data)
    if accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {format_data(accountA)}.")
    print(vs)
    print(f"Against B: {format_data(accountB)}.")

    guess = input("Who has the more followers : 'A' or 'B' ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = accountA["follower_count"]
    b_follower_count = accountB["follower_count"]

    is_correct = check(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False


