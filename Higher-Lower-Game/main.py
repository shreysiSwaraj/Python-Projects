import randon
from art import text2art
from game_data import data
import random

def account_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


logo = text2art("Higher Lower Game")

print(logo)

score = 0
i=0
while i<3:
    account_a = random.choice(data)
    account_b = random.choice(data)

    while True:
        if account_a == account_b:
            account_b = random.choice(data)
        else:
            break



    print(f"Compare {account_data(account_a)} Vs {account_data(account_b)}")
    prediction = input("Who has more followers ? Type 'A' or 'B'.").lower()

    if prediction == "a" and account_a["user_account"] > account_b["user_account"]:
        print(f"yay, you are right")
        score = score + 1
    elif prediction == "b" and account_b["user_account"] > account_a["user_account"]:
        print(f"yayy, you are right!")
        score = score + 1
    else:
        print(f"Sorry, you are wrong")

    i = i+1

print(f"Score: {score}")




