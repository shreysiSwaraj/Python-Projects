import os
from art import text2art

logo = text2art("Secret Auction")
print(logo)

bids = {}
bidding_over = False

def find_highest_bidder(bid_recorder):
    highest_bid = 0
    winner = ""
    for bidder in bid_recorder:
        bid_amount = bid_recorder[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'{winner} is the winner with highest bidding amount = ${highest_bid}')


while not bidding_over:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    ques = input("Is there any other user? Type 'yes' or 'no' ")
    if ques == "no":
        bidding_over = True
        find_highest_bidder(bids)
    elif ques == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')





